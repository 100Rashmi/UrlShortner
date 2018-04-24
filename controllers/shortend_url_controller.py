from datetime import datetime

from commons import constants
from commons.constants import URL_PREFIX
from commons.utils import convert_To_base_64, Logger
from db.db_connection import db_connection
from db.models import ShortendUrl


def create_shortend_url(long_url):
    shorturl = ShortendUrl()
    shorturl.long_url = long_url
    shorturl.created_time = datetime.utcnow()
    shorturl.status = constants.Status.INITIALIZE

    db_session = db_connection().get_session()

    db_session.add(shorturl)
    db_connection().commit()

    url_id = shorturl.url_id
    encoded_path = str(convert_To_base_64(url_id))

    updated_response = db_session.query(ShortendUrl).filter(ShortendUrl.url_id == url_id).update({ShortendUrl.status:constants.Status.ACTIVE, ShortendUrl.short_url: encoded_path})
    db_connection().commit()

    shorturl = URL_PREFIX+encoded_path
    return shorturl


def redirect_url(shortpath):
    db_session = db_connection().get_session()

    try:
        updated_count = db_session.query(ShortendUrl).filter(ShortendUrl.short_url == shortpath,
                                                             ShortendUrl.status == constants.Status.ACTIVE) \
            .update({ShortendUrl.status: constants.Status.EXPIRED})
        db_connection().commit()

        # case: when two user hit same time for same shortend url
        if updated_count > 0:
            url_info = db_session.query(ShortendUrl).filter(ShortendUrl.short_url == shortpath).first()
            return constants.Status.SUCCESS, url_info.long_url

        else:
            url_info_count = db_session.query(ShortendUrl).filter(ShortendUrl.short_url == shortpath).count()
            if url_info_count:
                return constants.Status.EXPIRED, 0
            else:
                return constants.Status.NOT_PRESENT, 0

    except Exception as ex:
        Logger().exception(ex)
        return constants.Status.UNKNOWN_ERROR, -1