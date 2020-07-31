def auto_filename_time(prefix='',sep='_',suffix='',ext='',
                       timeformat='%m-%d-%Y_%H%M%p'):
    '''Generates a filename with a  base string + sep+ the current datetime formatted as timeformat.
     filename = f"{prefix}{sep}{suffix}{sep}{timesuffix}{ext}
    '''
    from datetime import datetime
    from pytz import timezone

#     try:
    from tzlocal import get_localzone
    tz = get_localzone()
#     except:
#         print('tzlocal package not found, setting timezome=UTC')
#         tz= 'UTC'

    ## Get current time
    now = datetime.now(tz).strftime(timeformat)
    timesuffix = now.replace(':',sep).lower()
    
    filename = ''
    ## Construct filename in pieces
    if len(prefix)>0:
        filename +=f"{prefix}{sep}"# + filename
    
    if len(suffix)>0:
        filename +=f"{suffix}{sep}"

    filename+=f"{timesuffix}{ext}"
    return filename