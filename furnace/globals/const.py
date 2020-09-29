from furnace.globals.errors import ConstError


class ConstType(object):
    @property
    def index_page(self):
        return "index.html"

    @property
    def max_url_length(self):
        """
        Url over 2000 will not work in most of the popular browsers
        :return: int url max length
        """
        return 2000

    @property
    def ext_html(self):
        return '.html'

    @property
    def ext_html_template(self):
        return '.tpl.html'

const = ConstType()
