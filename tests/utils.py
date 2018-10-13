
def get_toolbar(app):
    return app.root.ids.toolbar


def get_manager(app):
    return app.root.ids.manager


def get_screen_element(app, element_id):
    return get_manager(app).current_screen.ids.get(element_id)


def get_toolbar_button(app, icon):
    right_actions = get_toolbar(app).ids.right_actions.children
    for btn in right_actions:
        if btn.icon == icon:
            return btn
