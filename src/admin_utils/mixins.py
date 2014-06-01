from django.contrib.admin import ModelAdmin


class FoldableListFilterAdminMixin(ModelAdmin):
    class Media:
        js = ['admin_utils/foldable-list-filter.js']
        css = {'all': ['admin_utils/foldable-list-filter.css']}


class FullWidthAdminMixin(ModelAdmin):
    class Media:
        css = {'all': ['admin_utils/full-width.css']}
