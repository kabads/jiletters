# Copyright Adam Cripps (2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2013)
# Licensed under the GNU GPL v2. 
# See https://www.gnu.org/licenses/gpl-2.0.html for more information. 

from wxPython.lib.grids import wxGridSizer, wxFlexGridSizer
from wxPython.wx import *
from sndhdr import *
from wave import *
import os, pygame, random
from pygame.locals import *
ID_BUTTON1=110

class MyFrame (wxFrame):
	def __init__(self, parent, ID, title):
		wxFrame.__init__(self,parent,wxID_ANY, title, style=wxDEFAULT_FRAME_STYLE|
                                        wxNO_FULL_REPAINT_ON_RESIZE)
		self.sizer2 = wxGridSizer(3,10,0,0)
		self.buttons=[]
		alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
		alphabetgraphics = ['a.bmp', 'b.bmp', 'c.bmp','d.bmp','e.bmp','f.bmp','g.bmp','h.bmp','i.bmp','j.bmp','k.bmp','l.bmp','m.bmp','n.bmp','o.bmp','p.bmp','q.bmp','r.bmp','s.bmp','t.bmp','u.bmp','v.bmp','w.bmp','x.bmp','y.bmp','z.bmp']
		for i in range(len(alphabet)):
			# print alphabetgraphics[i] #Debug
			bmp = wxBitmap('alphabet_graphics/' + alphabetgraphics[i], wxBITMAP_TYPE_BMP)
			self.grafic =wxBitmapButton(self,30 + i,bmp,wxPoint(160,20), wxSize(bmp.GetWidth()+10,bmp.GetHeight()+10))
			self.sizer2.Add(self.grafic,1,wxEXPAND)
			EVT_BUTTON(self,30+i, self.ButtonPushed)
		self.sizer=wxBoxSizer(wxVERTICAL)
		self.sizer.Add(self.sizer2,1,wxEXPAND) # This means that sizer is higher in the hierarchy than sizer 2
		#Layout sizers
		self.CreateStatusBar() # A Statusbar in the bottom of the window
		self.SetSizer(self.sizer)
		self.SetAutoLayout(1)
		self.sizer.Fit(self)
		self.Show(1)
		
		# And now for the menu
		menuBar = wxMenuBar() #Menu bar
		menu1 = wxMenu() # First menu
		menu1.Append(101, "&Exit", "Quit")
		menuBar.Append(menu1, "&File")
		self.SetMenuBar(menuBar)
		EVT_MENU(self, 101, self.Menu101)
		self.CenterOnScreen()

	def Menu101(self, evt):
		self.Destroy()
	
	def ButtonPushed(self, id):
		#print "button", id.GetId(), "was pushed" #Debug
		#print "object pushed", self # Debug
		letterframe = LetterFrame(None, -2, "Letter", id.GetId())
                if id.GetId()== 36:
                        # I could randomise this part to get two different sounds for particular sounds (e.g. hard and soft g)
                        if id.GetId()==36:
                                i = random.randint(0,1)
                                if i == 0:
                                        print "I will say the soft g"
                                        letterframe.SetBackgroundColour('Blue')
                                        letterframe.addtext(id.GetId())
                                        letterframe.Show(1)
                                else:
                                        print "I will say the hard g"
                                print str(i)
                
                else:
                        letterframe.SetBackgroundColour('Blue')
                        letterframe.addtext(id.GetId())
                        letterframe.Show(1)

class LetterFrame(wxFrame):
	def __init__(self,parent,ID,title, whichbutton):
		wxFrame.__init__(self,parent,wxID_ANY,title, pos=wxDefaultPosition, size=wxDefaultSize,style=wxDEFAULT_DIALOG_STYLE)
		
	def addtext(self,text):
		#showtext = str(text) # wxStaticText needs a string
		alphabetgraphics = {30:'angelfish.bmp',31:'balloons.bmp',32:'crocodile.bmp',33:'dog.bmp',34:'eagle.bmp',35:'frog.bmp',36:'giraffe.bmp',37:'horse.bmp',38:'igloo.bmp',39:'jester.bmp',40:'kangaroo.bmp',41:'lizard.bmp',42:'moose.bmp',43:'nest.bmp',44:'octopus.bmp',45:'penguin.bmp',46:'queen.bmp',47:'rhinoceros.bmp',48:'seal.bmp',49:'tiger.bmp',50:'umbrella.bmp',51:'vulture.bmp',52:'wolf.bmp',53:'fox.bmp',54:'yacht.bmp',55:'zebra.bmp'}
		bmp = wxBitmap('alphabet_media/' + alphabetgraphics[text], wxBITMAP_TYPE_BMP)
		newID = text +50
		self.button = wxBitmapButton(self, newID, bmp, wxPoint(160,20), wxSize(bmp.GetWidth()+10,bmp.GetHeight()+10))
		self.buttonsizer = wxGridSizer(1,1,0,0)
		
		self.buttonsizer.Add(self.button,1,wxEXPAND)
		EVT_BUTTON(self.button,newID, self.delete)


		self.labelsizer =wxGridSizer(1,1,0,0)
		label = {30:'a, Angelfish', 31:'b, Balloons', 32:'c, Crocodile', 33:'d, Dog', 34:'e, Eagle', 35:'f, Frog', 36:'g, Giraffe', 37:'h, Horse', 38:'i, Igloo', 39:'j, Jester', 40:'k, Kangaroo', 41:'l, Lizard', 42:'m, Moose', 43:'n, nest', 44:'o, Octopus', 45:'p, Penguin', 46:'q, Queen', 47:'r, Rhinoceros', 48:'s, Seal', 49:'t, Tiger', 50:'u, Umbrella', 51:'v, Vulture', 52:'w, Wolf', 53:'x, Fox', 54:'y, yacht', 55:'z, Zebra'}
		showtext = str(label[text]) # wxStaticText needs a string
		self.labeltext = wxStaticText(self, -11, showtext, (20, 10),style=wxALIGN_CENTRE) #.SetBackgroundColour('White')
		font = wxFont(18, wxSWISS, wxNORMAL, wxNORMAL)
		self.labeltext.SetFont(font)
		self.labeltext.SetBackgroundColour('Yellow')
		self.labelsizer.Add(self.labeltext,1,wxEXPAND)
		
		self.mastersizer = wxBoxSizer(wxVERTICAL)
		self.mastersizer.Add(self.buttonsizer,1,wxEXPAND)
		self.mastersizer.Add(self.labelsizer,0,wxEXPAND)
		self.SetSizer(self.mastersizer)
		self.SetAutoLayout(1)
		self.mastersizer.Fit(self)
		self.MakeModal(1)
		self.CentreOnScreen


		sounds = {30:'a.wav', 31:'b.wav', 32:'c.wav', 33:'d.wav', 34:'e.wav', 35:'f.wav', 36:'g.wav', 37:'h.wav', 38:'i.wav', 39:'j.wav', 40:'k.wav', 41:'l.wav', 42:'m.wav', 43:'n.wav', 44:'o.wav', 45:'p.wav', 46:'q.wav', 47:'r.wav', 48:'s.wav', 49:'t.wav', 50:'u.wav', 51:'v.wav', 52:'w.wav', 53:'x.wav', 54:'y.wav', 55:'z.wav'}
		#sound_file = 'sound_media/' + sounds[text]
		sound_file = sounds[text]
		pygame.mixer.init()

		def load_sound(name):
			class NoneSound:
				def play(self): pass
			if not pygame.mixer or not pygame.mixer.get_init():
				return NoneSound()
			fullname = os.path.join('sound_media', name)
			try:
				sound = pygame.mixer.Sound(fullname)
			except pygame.error, message:
				print 'Cannot load sound:', fullname
				raise SystemExit, message
			return sound



#filename = open('a.wav', 'rb')
		mysound = load_sound(sound_file)
		mysound.play()
		#pygame.time.delay(2000)



	def delete (self, *ignored):
		#print 'goodbye'
		#print self # Debug
		self.MakeModal(0) # Must turn off modal, otherwise app doesn't respond
		self.Destroy()


	

app = wxPySimpleApp()
frame = MyFrame(None, -1, "JILetters")
frame.Show(1)
app.MainLoop()
print "You are running version 0.07"

# Will be using these colours for the buttons
#456C93 #69A5E0 #948746 #E0B969 #6B6B6B #949494 
# 
