scrapy-tg-export
===================

``scrapy-tg-export`` package provides a Scrapy extension to send items
to Telegram.

License is MIT.

Extension requires Python 2.7 or 3.5+.

Usage
-----

To use TGItemExporterExtension, enable and configure it in settings.py::

    EXTENSIONS = {
        'scrapy_tg_export.TGItemExporterExtension': 1,
    }
    TELEGRAM_EXPORT_ENABLED = True
    TELEGRAM_API_KEY = <telegram bot API key>
    TELEGRAM_CHAT_ID = <telegram chat id (with minus sign)>
    TELEGRAM_MESSAGE_PREPROCESSOR = <(optional) your function to convert Item into markdown text>

After that all scraped items would be put to a specified Telegram chat.

Message preprocessor takes item and response as input, returns string representation and boolean export flag.
If this flag is False then item won't be exported.  
 
