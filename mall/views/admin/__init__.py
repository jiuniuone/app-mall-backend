from collections import OrderedDict

from django.contrib.auth.mixins import AccessMixin

from acmin.utils import Field, attr, get_ancestors, get_model_fields, import_submodules
from acmin.views.admin import *
from mall.models import Role, User


class StaticMixin(StaticFilterMixin):

    def get_max_cls(self):
        return super().get_max_cls()

    def get_static_filter(self):
        return super().get_static_filter()


class UserCheckMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        user: User = request.user
        has_permission = user.is_authenticated

        if has_permission:
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()


class ContextMixin(object):
    @property
    def user(self) -> User:
        return attr(self, "request.user")

    @property
    def is_creatable(self) -> bool:
        return self.model.creatable

    @property
    def is_cloneable(self) -> bool:
        return self.is_creatable

    @property
    def is_editable(self) -> bool:
        return self.model.editable

    @property
    def is_removable(self) -> bool:
        return self.model.removable

    @property
    def is_viewable(self) -> bool:  # 是否可以查看详情页,但不能编辑
        return True

    @property
    def is_operable(self) -> bool:
        return self.is_editable or self.is_removable

    @property
    def is_selectable(self) -> bool:
        return False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'model_name': self.model.__name__,
            'model_verbose_name': attr(self, 'model._meta.verbose_name'),
            'creatable': self.is_creatable,
            'cloneable': self.is_cloneable,
            'editable': self.is_editable,
            'viewable': self.is_editable,
            'removable': self.is_removable,
            'operable': self.is_operable,
            "selectable": self.is_selectable,
        })
        return context


class BaseCreateView(StaticMixin, UserCheckMixin, ContextMixin, AdminCreateView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_form_kwargs(self):
        return super().get_form_kwargs()

    pass


class BaseUpdateView(StaticMixin, UserCheckMixin, ContextMixin, AccessMixin, AdminUpdateView):
    pass


class BaseListView(StaticMixin, UserCheckMixin, ContextMixin, AdminListView):
    def get_accestor_search_fields(self):
        return super().get_accestor_search_fields()

    def get_model_exclude_names(self):
        return attr(self.model, "list_exclude", [])

    def get_model_include_names(self):
        return attr(self.model, "list_fields")

    def get_model_list_fields(self):
        cls = self.model
        names = self.get_model_include_names()
        model_fields = get_model_fields(cls)
        field_dict = OrderedDict([(f.name, f) for f in model_fields])
        if names == '__all__' or not names:
            names = [f.name for f in model_fields]
        excludes = self.get_model_exclude_names()
        excludes = excludes + ['id', 'created', 'modified'] + [
            f.name for f in model_fields if f.related_model
        ]
        result = []
        for name in names:
            verbose_name = None
            orderable = True
            if isinstance(name, tuple):
                name, verbose_name = name
                orderable = False
            if name not in excludes:
                if not verbose_name:
                    verbose_name = field_dict[name].verbose_name if name in field_dict else name
                field = Field(name, verbose_name, name, None, orderable)
                result.append(field)

        return result

    def get_parent_list_fields(self):
        fields = []
        model = self.model
        chains = get_ancestors(model, self.get_max_cls())
        chain_names = [name for name, _ in chains]
        count = len(chains)


        for index in range(0, count):
            name, model = chains[index]
            attribute_name = ".".join(chain_names[0:chain_names.index(name) + 1])
            fields.append(Field(name, attr(model, "_meta.verbose_name"), attribute_name, model.__name__))

        fields.reverse()
        return fields

    def get_list_fields(self):
        parent_fields = self.get_parent_list_fields()

        return parent_fields + self.get_model_list_fields()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"list_fields": self.get_list_fields(), })
        return context


class BaseExportView(StaticMixin, ContextMixin, UserCheckMixin, AdminExportView):
    pass


class BaseDeleteView(UserCheckMixin, AdminDeleteView):
    pass


import_submodules(locals(), __name__, __path__)
