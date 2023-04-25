class RenderList:
    def __init__(self, type_list='ul'):
        self.type_list = type_list

    def __call__(self, lst, *args, **kwargs):
        return "\n".join([f'<{self.type_list}>', *map(lambda x: f'<li>{x}</li>', lst ), f'</{self.type_list}>'])


lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("ul")
html = render(lst)
print(html)
