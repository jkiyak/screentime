select generation, count(*), avg(daily_screen_time_hours), avg(social_media_hours)
from screentime_data
group by generation;

