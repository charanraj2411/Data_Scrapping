from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout


Builder.load_file('checkbox.kv')
SortBy=[]
DatePosted=[]
ExpLevel=[]
JobLevel=[]
Work_Mode=[]

class MyLayout(BoxLayout):
    
    def SortBy_click(self,instance,value,filter_input):
        if value==True:
            SortBy.append(filter_input)
            self.ids.output_label.text=f'You selected : {SortBy}'
        else:
            SortBy.remove(filter_input)
            self.ids.output_label.text=f'You selected : {SortBy}'

    
    def DatePosted_click(self,instance,value,filter_input):
        if value==True:
            DatePosted.append(filter_input)
            self.ids.output_label.text=f'You selected : {DatePosted}'
        else:
            DatePosted.remove(filter_input)
            self.ids.output_label.text=f'You selected : {DatePosted}'

    
    def Exp_click(self,instance,value,filter_input):
        if value==True:
            ExpLevel.append(filter_input)
            self.ids.output_label.text=f'You selected : {ExpLevel}'
        else:
            ExpLevel.remove(filter_input)
            self.ids.output_label.text=f'You selected : {ExpLevel}'

    
    def JobLevel_click(self,instance,value,filter_input):
        if value==True:
            JobLevel.append(filter_input)
            self.ids.output_label.text=f'You selected : {JobLevel}'
        else:
            JobLevel.remove(filter_input)
            self.ids.output_label.text=f'You selected : {JobLevel}'


      
    def WorkMode_click(self,instance,value,filter_input):
        if value==True:
            Work_Mode.append(filter_input)
            self.ids.output_label.text=f'You selected : {Work_Mode}'
        else:
            Work_Mode.remove(filter_input)
            self.ids.output_label.text=f'You selected : {Work_Mode}'

class AwesomeApp(App):
    def build(self):
        return MyLayout()


if __name__=='__main__':
    AwesomeApp().run()
    print(SortBy)
    print(DatePosted)
    print(ExpLevel)
    print(JobLevel)
    print(Work_Mode)