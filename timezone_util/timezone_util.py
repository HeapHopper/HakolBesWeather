from timezonefinder import TimezoneFinder
from datetime import datetime, timezone
import pytz

def location_to_tz_util(lat,lon):
    tf = TimezoneFinder()
    tz_str = tf.timezone_at(lat=lat, lng=lon)
    if tz_str:
        return tz_str
    else:
        return 'Asia/Jerusalem'


def get_local_time(timezone_name) -> str:

    if timezone_name:
        # Get the timezone object
        target_timezone = pytz.timezone(timezone_name)

        # Get the current UTC time using timezone-aware method
        utc_now = datetime.now(timezone.utc)

        # Convert UTC time to the target timezone
        local_time = utc_now.astimezone(target_timezone)

        return local_time.strftime("%Y-%m-%d %H:%M:%S")  # Format with timezone info

    else:
        return "Timezone could not be determined for the given coordinates."

if __name__ == '__main__':
    print(location_to_tz_util(31.7788242,35.2257626))
    print(get_local_time(location_to_tz_util(31.7788242,35.2257626)))

    print(location_to_tz_util(35.652832, 139.839478))
    print(get_local_time(location_to_tz_util(35.652832, 139.839478)))

    print(location_to_tz_util(44.412266, -110.723183))
    print(get_local_time(location_to_tz_util(44.412266, -110.723183)))
