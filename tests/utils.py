
def get_screen_element( app, element_id):
    return app.root.ids.manager.current_screen.ids.get(element_id)


def get_toolbar_button( app, icon):
    right_actions = app.root.ids.toolbar.ids.right_actions.children
    for btn in right_actions:
        if btn.icon == icon:
            return btn
