from site_element import SiteElement


class HomePage:
    def __init__(self):
        self.to_discover = SiteElement('li', el_id='dropdown-menu-search')
        self.to_apps = SiteElement('*', el_id='dropdown-menu-' +
                                   'https:--www.hydroshare.org-apps-')


class AppsPage:
    def __init__(self):
        self.container = \
            SiteElement('div', el_class='container apps-container',
                        el_recursive=[SiteElement('div', el_class='row')])

    def info(self, num):
        return SiteElement('div', el_class='container apps-container',
                           el_recursive=(
                               [SiteElement('div', el_class='row'),
                                SiteElement('div[' + str(num) + ']'),
                                SiteElement('a',
                                            el_class='app-info-toggle')]))

    def resource(self, num):
        return SiteElement('div', el_class='container apps-container',
                           el_recursive=(
                               [SiteElement('div', el_class='row'),
                                SiteElement('div[' + str(num) + ']'),
                                SiteElement('p', el_class='app-description'),
                                SiteElement('a')]))

    def title(self, num):
        return SiteElement('div', el_class='container apps-container',
                           el_recursive=(
                               [SiteElement('div', el_class='row'),
                                SiteElement('div[' + str(num) + ']'),
                                SiteElement('h3')]))


class DiscoverPage:
    def __init__(self):
        self.start_date = SiteElement('input', el_id='id_start_date')
        self.end_date = SiteElement('input', el_id='id_end_date')
        self.map_tab = SiteElement('a', el_href='map-view')
        self.map_search = SiteElement('input', el_id='geocoder-address')
        self.map_submit = SiteElement('a', el_id='geocoder-submit')
        self.list_tab = SiteElement('a', el_content='List')
        self.sort_order = SiteElement('select', el_id='id_sort_order')
        self.sort_direction = SiteElement('select',
                                          el_id='id_sort_direction')
        self.col_headers = SiteElement('table', el_id='items-discovered',
                                       el_recursive=[SiteElement('thead'),
                                                     SiteElement('tr')])

    def to_resource(self, title):
        return SiteElement('a', el_content=title)

    def col_index(self, col_index):
        """ Return the column header element, given the index """
        return SiteElement('table', el_id='items-discovered',
                           el_recursive=[SiteElement('thead'),
                                         SiteElement('tr'),
                                         SiteElement('th[' +
                                                     str(col_index) + ']')])

    def cell(self, col, row):
        """ Return the cell in the discover table, given row and column
        indicies
        """
        return SiteElement('table', el_id='items-discovered',
                           el_recursive=[SiteElement('tbody'),
                                         SiteElement('tr[' +
                                                     str(row) + ']'),
                                         SiteElement('td[' +
                                                     str(col) + ']')])

    def cell_href(self, col, row):
        """ Return the cell in the discover table, given row and column
        indicies.  Builds on discover_field method, but enables use for
        hyperlinked fields.
        """
        return SiteElement('table', el_id='items-discovered',
                           el_recursive=[SiteElement('tbody'),
                                         SiteElement('tr[' +
                                                     str(row) + ']'),
                                         SiteElement('td[' +
                                                     str(col) + ']'),
                                         SiteElement('a')])

    def cell_strong_href(self, col, row):
        """ Return the cell in the discover table, given row and column
        indicies.  Builds on discover_field method, but enables use for
        bolded and hyperlinked fields.
        """
        return SiteElement('table', el_id='items-discovered',
                           el_recursive=[SiteElement('tbody'),
                                         SiteElement('tr[' +
                                                     str(row) + ']'),
                                         SiteElement('td[' +
                                                     str(col) + ']'),
                                         SiteElement('strong'),
                                         SiteElement('a')])

    def filter_author(self, author):
        return SiteElement('input', el_id='creators-' + author)

    def filter_subject(self, subject):
        return SiteElement('input', el_id='subjects-' + subject)

    def filter_resource_type(self, resource_type):
        return SiteElement('input', el_id='resource_type-' + resource_type)

    def filter_owner(self, owner):
        return SiteElement('input', el_id='owners_names-' + owner)

    def filter_variable(self, variable):
        return SiteElement('input', el_id='variable_names-' + variable)

    def filter_sample_medium(self, sample_medium):
        return SiteElement('input', el_id='sample_mediums-' + sample_medium)

    def filter_unit(self, unit):
        return SiteElement('input', el_id='units_names-' + unit)

    def filter_discoverable(self, discoverable):
        return SiteElement('input', el_id='discoverable-' + discoverable)

    def filter_public(self, public):
        return SiteElement('input', el_id='public-' + public)

    def filter_availability(self, availability):
        return SiteElement('input', el_id=availability + '-true')


class ResourcePage:
    def __init__(self):
        self.bagit = SiteElement('a', el_id='btn-download-all',
                                 el_content='Download All Content as ' +
                                 'Zipped BagIt Archive')


HomePage = HomePage()
AppsPage = AppsPage()
DiscoverPage = DiscoverPage()
ResourcePage = ResourcePage()