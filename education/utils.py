class DataMixin:
    title_page = None
    extra_context = {}
    paginate_by = 3
    category = None

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.category:
            self.extra_context['category'] = self.category

    def get_mixin_data(self, context, **kwargs):
        context['title'] = kwargs['title']
        context['category'] = kwargs['category']

        return context
