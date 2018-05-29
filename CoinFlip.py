### Boring Legal Stuff ###

#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  CoinFlip.py
#  
#  Copyright 2018 user1 <user1@USER1-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

### The actual program stuff ###

#######################################################################
# CoinFlip.py
#
# This is a simple program that will do some coin flipping
# and output some stats on the coins that were flipped
# including total coins flipped, total heads, total tails,
# and the most heads / tails flipped in a row
#
# Made in Geany using Kivy and Python 3

import kivy
kivy.require("1.10.0")
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import random

# Main
# Builds the kv file instead of having it separate
class Main(App):
	def build(self):
		Builder.load_string(
"""
Container:

#Container holds all the other layouts
<Container>:
	id: contain
	orientation: "vertical"
	#pos_hint: {'center_y': 0.5, 'center_x': 0.5}
	#size_hint_y: None
	#height: 0.5625 * root.width
	StartMenu
	
<StartMenu>:
	orientation: "vertical"
	Button:
		text: "Coin Flip"
		on_press: root.goto_coin_menu()
	Button:
		text: "Exit"
		on_press: root.quit_game()
		
<CoinMenu>:
	orientation: "vertical"
	BoxLayout:
		size_hint_y: 0.05
		orientation: "horizontal"
		Label:
			text: "Coins: "
		TextInput:
			id: coinInput
			text: "100"
			multiline: False
	Button:
		size_hint_y: 0.2
		text: "Flip!"
		font_size: "30sp"
		on_press: root.flip_coins()
	BoxLayout:
		orientation: "vertical"
		size_hint_y: 0.5
		id: CoinOutput
		BoxLayout:
			orientation: "horizontal"
			Label:
				id: CoinsFlippedText
				text_size: self.width, self.height
				size: self.texture_size
				valign: "top"
				halign: "right"
				text: "Coins flipped: "
				
			Label:
				id: CoinsFlippedNumber
				text_size: self.width, self.height
				size: self.texture_size
				valign: "top"
				halign: "left"
				text: "0"
				
		BoxLayout:
			orientation: "horizontal"
			Label:
				id: HeadsText
				text_size: self.width, self.height
				size: self.texture_size
				valign: "top"
				halign: "right"
				text: "Total Heads: "
				
			Label:
				id: HeadsNumber
				text_size: self.width, self.height
				size: self.texture_size
				valign: "top"
				halign: "left"
				text: "0"
				
		BoxLayout:
			orientation: "horizontal"
			Label:
				id: TailsText
				text_size: self.width, self.height
				size: self.texture_size
				valign: "top"
				halign: "right"
				text: "Total Tails: "
				
			Label:
				id: TailsNumber
				text_size: self.width, self.height
				size: self.texture_size
				valign: "top"
				halign: "left"
				text: "0"
				
		BoxLayout:
			orientation: "horizontal"			
			Label:
				id: HeadsComboText
				text_size: self.width, self.height
				size: self.texture_size
				valign: "top"
				halign: "right"
				text: "Most Heads In A Row: "
				
			Label:
				id: HeadsComboNumber
				text_size: self.width, self.height
				size: self.texture_size
				valign: "top"
				halign: "left"
				text: "0"
				
		BoxLayout:
			orientation: "horizontal"			
			Label:
				id: TailsComboText
				text_size: self.width, self.height
				size: self.texture_size
				valign: "top"
				halign: "right"
				text: "Most Tails In A Row: "
				
			Label:
				id: TailsComboNumber
				text_size: self.width, self.height
				size: self.texture_size
				valign: "top"
				halign: "left"
				text: "0"
				
	Button:
		size_hint_y: 0.1
		text: "Back"
		on_press: root.goto_start_menu()
""")
		global root
		root = Container()
		return root

# The primary gui piece that holds all the other gui pieces
class Container(BoxLayout):
	pass

# The first menu the user sees
class StartMenu(BoxLayout):
	def quit_game(self):
		App.get_running_app().stop()
	def goto_coin_menu(self):
		root.clear_widgets()
		root.add_widget(CoinMenu())

# The bulk of the coin flip program, this is where stuff happens
# Flipping more than a million coins can be laggy
class CoinMenu(BoxLayout):	
	def goto_start_menu(self):
		root.clear_widgets()
		root.add_widget(StartMenu())
		
	def flip_coins(self):
		total = 0
		heads = 0    		#total number of heads
		headsCombo = 0 		#current heads combo
		headsComboBest = 0 	#best heads combo
		tails = 0			#total number of tails
		tailsCombo = 0		#current tails combo
		tailsComboBest = 0	#best heads combo
		currentCombo = 0 	#whether its a heads or tails combo

		i = int(self.ids['coinInput'].text)
		while i >= 1:
			total += 1
			flip = random.randint(1,2)
			if flip == 1:
				heads += 1
				if(currentCombo != 1):
					currentCombo = 1
					tailsCombo = 0
					headsCombo = 1
				else:
					headsCombo += 1
					if headsCombo > headsComboBest:
						headsComboBest = headsCombo
			elif flip == 2:
				tails += 1
				if(currentCombo != 2):
					currentCombo = 2
					tailsCombo = 1
					headsCombo = 0
				else:
					tailsCombo += 1
					if tailsCombo > tailsComboBest:
						tailsComboBest = tailsCombo
			i -= 1
		
		total = str(heads + tails)
		self.ids['CoinsFlippedNumber'].text = total
		self.ids['HeadsNumber'].text = str(heads)
		self.ids['TailsNumber'].text = str(tails)
		self.ids['HeadsComboNumber'].text = str(headsComboBest)
		self.ids['TailsComboNumber'].text = str(tailsComboBest)
		

	
# Runs the program	
if __name__ == '__main__':
	Main().run()
	
	
	
	
	
