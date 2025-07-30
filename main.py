from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
from current import Current
import hearing

# Set the app size
Window.size = (500,700)

# Designate Our .kv design file 
Builder.load_file('main.kv')

current = Current()

class MyLayout(Widget):

   #Right kHz input

   def right_one(root):
      current.set(root.ids.right_one_k)

   def right_two(root):
      current.set(root.ids.right_two_k)

   def right_three(root):
      current.set(root.ids.right_three_k)

   def right_four(root):
      current.set(root.ids.right_four_k)

   def right_six(root):
      current.set(root.ids.right_six_k)

   def right_eight(root):
      current.set(root.ids.right_eight_k)

   def get_right_three(root):
       return [root.ids.right_one_k, root.ids.right_two_k, root.ids.right_three_k]
   
   def get_right_eight(root):
       return [root.ids.right_four_k, root.ids.right_six_k, root.ids.right_eight_k]
   
   def get_right(root):
       return root.get_right_three() + root.get_right_eight()
   
   #Left kHz input

   def left_one(root):
      current.set(root.ids.left_one_k)

   def left_two(root):
      current.set(root.ids.left_two_k)

   def left_three(root):
      current.set(root.ids.left_three_k)

   def left_four(root):
      current.set(root.ids.left_four_k)

   def left_six(root):
      current.set(root.ids.left_six_k)

   def left_eight(root):
      current.set(root.ids.left_eight_k)

   def get_left_three(root):
       return [root.ids.left_one_k, root.ids.left_two_k, root.ids.left_three_k]
   
   def get_left_eight(root):
       return [root.ids.left_four_k, root.ids.left_six_k, root.ids.left_eight_k]
   
   def get_left(root):
       return root.get_left_three() + root.get_left_eight()
   
   #Final row

   def press_age(root):
      current.set(root.ids.age_input)

   def press_back(root):
       current.back()

   def zero(root):
       current.add("0")
   
   def one(root):
      current.add("1")
      
   def two(root):
      current.add("2")

   def three(root):
      current.add("3")

   def four(root):
      current.add("4")

   def five(root):
      current.add("5")

   def six(root):
      current.add("6")

   def seven(root):
      current.add("7")

   def eight(root):
      current.add("8")

   def nine(root):
      current.add("9")

   def male_press(root):
       root.ids.male_button.background_color = (1, 0, 0, 1)
       root.ids.female_button.background_color = (157/255, 157/255, 157/255, 1)

   def female_press(root):
       root.ids.female_button.background_color = (1, 0, 0, 1)
       root.ids.male_button.background_color = (157/255, 157/255, 157/255, 1)

   def twenty_five_press(root):
       root.ids.twenty_five_button.background_color = (1, 0, 0, 1)
       root.ids.fifty_button.background_color = (157/255, 157/255, 157/255, 1)
       root.ids.seventy_five_button.background_color = (157/255, 157/255, 157/255, 1)

   def fifty_press(root):
       root.ids.twenty_five_button.background_color = (157/255, 157/255, 157/255, 1)
       root.ids.fifty_button.background_color = (1, 0, 0, 1)
       root.ids.seventy_five_button.background_color = (157/255, 157/255, 157/255, 1)

   def seventy_five_press(root):
       root.ids.seventy_five_button.background_color = (1, 0, 0, 1)
       root.ids.fifty_button.background_color = (157/255, 157/255, 157/255, 1)
       root.ids.twenty_five_button.background_color = (157/255, 157/255, 157/255, 1)

   #Visual functions
   
   def set_out(root):
       right = root.get_right()
       left = root.get_left()

       for i in range(0,6):
           right[i].text = str(hearing.frequency[i]) + "kHz: "
           left[i].text = str(hearing.frequency[i]) + "kHz: "

       root.ids.enter.text = "Enter"

       root.ids.age_input.text = "Age: "

       root.ids.male_button.state = 'normal'
       root.ids.female_button.state = 'normal'

       root.ids.male_button.text = "Male"
       root.ids.female_button.text = "Female"

       root.ids.twenty_five_button.text = '25%'
       root.ids.fifty_button.text = '50%'
       root.ids.seventy_five_button.text = '75%'

       root.ids.twenty_five_button.disabled = False
       root.ids.fifty_button.disabled = False
       root.ids.seventy_five_button.disabled = False

       root.ids.male_button.disabled = False
       root.ids.female_button.disabled = False

       current.set(root.ids.right_one_k)

   def output_layout(root, output):

       root.ids.twenty_five_button.text = ""
       root.ids.fifty_button.text = ""
       root.ids.seventy_five_button.text = ""

       root.ids.male_button.text = ""
       root.ids.female_button.text = ""

       root.ids.twenty_five_button.disabled = True
       root.ids.fifty_button.disabled = True
       root.ids.seventy_five_button.disabled = True

       root.ids.male_button.disabled = True
       root.ids.female_button.disabled = True
       root.ids.enter.text = "Reset"

       root.ids.twenty_five_button.state = 'normal'
       root.ids.fifty_button.state = 'normal'
       root.ids.seventy_five_button.state = 'normal'

       root.ids.twenty_five_button.background_color = (157/255, 157/255, 157/255, 1)
       root.ids.fifty_button.background_color = (157/255, 157/255, 157/255, 1)
       root.ids.seventy_five_button.background_color = (157/255, 157/255, 157/255, 1)  

       root.ids.male_button.state = 'normal'
       root.ids.female_button.state = 'normal'

       root.ids.male_button.background_color = (157/255, 157/255, 157/255, 1)
       root.ids.female_button.background_color = (157/255, 157/255, 157/255, 1)

       root.ids.age_input.background_color = (157/255, 157/255, 157/255, 1)

       root.ids.age_input.text = str(round(output, 2)) + " dB"
       

   def set_CLB(root):
       root.ids.black_book.disabled = False
       root.ids.DHSS.disabled = False
       root.ids.CLB.disabled = True

       right = root.get_right_eight()
       left = root.get_left_eight()

       for i in range(0,3):
           right[i].disabled = True
           left[i].disabled = True

       root.set_out()
   
   def set_DHSS(root):
       root.ids.black_book.disabled = False
       root.ids.DHSS.disabled = True
       root.ids.CLB.disabled = False

       right = root.get_right_eight()
       left = root.get_left_eight()

       for i in range(0,3):
           right[i].disabled = False
           left[i].disabled = False

       root.set_out()

   def enter_press(root):
       if root.ids.enter.text == "Enter":
         
         try:
            age = int(root.ids.age_input.text[5:])
         except ValueError:
            age = 0

         if root.ids.male_button.state == 'down':
            sex = "m"
         elif root.ids.female_button.state == 'down':
            sex = "f"
         else:
            sex = False

         if root.ids.twenty_five_button.state == 'down':
            fq = 25
         elif root.ids.fifty_button.state == 'down':
            fq = 50
         elif root.ids.seventy_five_button.state == 'down':
            fq = 75
         else:
            fq = False

         if root.ids.DHSS.disabled == True:

            right = root.get_right()
            left = root.get_left()

            right_data = []
            left_data = []

            for i in range(0,6):
                right_data.append(int(right[i].text[5:]))
                left_data.append(int(left[i].text[5:]))

            output = hearing.calculateDHSS(right_data, left_data, age, sex, fq)

         if root.ids.CLB.disabled == True:
             
            right = root.get_right_three()
            left = root.get_left_three()

            right_data = []
            left_data = []

            for i in range(0,3):
                right_data.append(int(right[i].text[5:]))
                left_data.append(int(left[i].text[5:]))

            output = hearing.calculateCLB(right_data, left_data, age, sex, fq)
            
         if output != False:
             
             root.output_layout(output)

       else:
         root.set_out()

class HearingApp(App):
	def build(self):
		return MyLayout()

if __name__ == '__main__':
	HearingApp().run()

