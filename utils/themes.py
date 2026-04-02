class Themes:
    light = {
        'bg': '#f0f0f0',
        'fg': '#000000',
        'button_bg': '#e1e1e1',
        'entry_bg': '#ffffff',
        'tree_bg': '#ffffff',
        'tree_fg': '#000000'
    }

    dark = {
        'bg': '#2d2d2d',
        'fg': '#ffffff',
        'button_bg': '#4d4d4d',
        'entry_bg': '#3d3d3d',
        'tree_bg': '#3d3d3d',
        'tree_fg': '#ffffff'
    }

    current = light

    @classmethod
    def toggle(cls):
        cls.current = cls.dark if cls.current == cls.light else cls.light
        return cls.current