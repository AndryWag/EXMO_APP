import EXMO_API
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

#kv codes
Builder.load_string('''
<DataTable>:
    id: main_win
    RecycleView:
        viewclass: 'CustomLabel'
        id: table_floor
        RecycleGridLayout:
            id: table_floor_layout
            cols: 5
            default_size: (None,250)
            default_size_hint: (1,None)
            size_hint_y: None
            height: self.minimum_height
            spacing: 5
<CustomLabel@Label>:
    bcolor: (1,1,1,1)
    canvas.before:
        Color:
            rgba: root.bcolor
        Rectangle:
            size: self.size
            pos: self.pos
''')

class DataTable(BoxLayout):
    def __init__(self, API_data=0, **kwargs):
        super().__init__(**kwargs)
        data = API_data.data
        pair = API_data.pair

        table_data = []
        table_data.append({'text':str(API_data.pair),'size_hint_y':None,'height':30,'bcolor':(.50,.30,.80,1)})
        table_data.append({'text':str(''),'size_hint_y':None,'height':30,'bcolor':(.50,.30,.80,1)})


        self.columns = 2

        for key in data:
            table_data.append({'text':str(key),'size_hint_y':None,'height':30,'bcolor':(.05,.30,.80,1)})
            table_data.append({'text':str(data[key]),'size_hint_y':None,'height':30,'bcolor':(.05,.30,.80,1)})
        self.ids.table_floor_layout.cols = self.columns #define value of cols to the value of self.columns
        self.ids.table_floor.data = table_data #add table_data to data value

class DataTableApp(App):
    def build(self):
        data = EXMO_API.EXMO_API()
        data.get_pair_data()
        return DataTable(data)

if __name__=='__main__':
    DataTableApp().run()
