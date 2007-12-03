# -*- coding: utf-8 -*-

# Copyright (C) 2003-2006 by Igor E. Novikov
# Copyright (C) 1997, 1998, 1999, 2000, 2001, 2002, 2003 by Bernhard Herzog
#
# This library is covered by GNU Library General Public License.
# For more info see COPYRIGHTS file in sK1 root directory.

from app.UI.Ttk import TFrame, TLabel
from Tkinter import LEFT, RIGHT
from app.conf.const import SELECTION, MODE
from guides_panel import GuidesPanel
from resize_panel import ResizePanel
from rotation_panel import RotatePanel
from flip_panel import FlipPanel
from unit_panel import UnitPanel
from page_panel import PagePanel
from group_panel import GroupPanel, CombinePanel, ToCurvePanel
from subpanel import CtxSubPanel

UNKNOWN_OBJ=-1
GROUP=0
RECTANGLE=1
BEZIER=2
ELLIPSE=3
IMAGE=4
SIMPLE_TEXT=5

SelectionMode=0
EditMode=1

forPage=['PagePanel', 'UnitPanel','GuidesPanel']
forObject=['ResizePanel','UnitPanel','FlipPanel', 'RotatePanel', 'CombinePanel', 'ToCurvePanel']
forGroup=['ResizePanel','UnitPanel','FlipPanel', 'RotatePanel', 'GroupPanel', 'CombinePanel', 'ToCurvePanel']

class ContexPanel:
	
	panelRegistry={}
	currentContent=[]
	current_type=''
	
	def __init__(self, parent, mainwindow):
		self.parent=parent
		self.mainwindow=mainwindow
		self.panel=TFrame(self.parent, name = 'ctxPanel', style='ToolBarFrame', borderwidth=2)
		label = TLabel(self.panel, image = "toolbar_left")
		label.pack(side = LEFT)
		self.mainwindow.document.Subscribe(SELECTION, self.check)
		self.mainwindow.document.Subscribe(MODE, self.check)
		self.initPanels()
		self.changeContent(forPage)
		
	def initPanels(self):
		for panel in PanelList:
			self.panelRegistry[panel.name]=panel(self)
			
	def changeContent(self, panelgroup):
		if not self.current_type==panelgroup:
			if len(self.currentContent):
				for panel in self.currentContent:
					panel.panel.forget()		
				self.currentContent[-1].setNormal()
				self.currentContent=[]
			for panelname in panelgroup:
				self.currentContent.append(self.panelRegistry[panelname])
				self.panelRegistry[panelname].panel.pack(side = LEFT)
			self.currentContent[-1].setLast()
			self.current_type=panelgroup
		
	def check(self):
		doc=self.mainwindow.document
		mode=doc.Mode()
		content=forPage
		selinf=doc.selection.GetInfo()		
		if len(selinf)==0:
			self.changeContent(forPage)
		elif len(selinf)==1:	
			obj_type=self.checkObject(selinf[0][-1])
			if mode==SelectionMode:
				if obj_type==GROUP:
					self.changeContent(forGroup)
				else:
					self.changeContent(forObject)
			else:
				if obj_type==GROUP:
					self.changeContent(forGroup)
				else:
					self.changeContent(forObject)	
		else:
			if mode==SelectionMode:
				self.changeContent(forGroup)
			else:
				self.changeContent(forGroup)
	
	def checkObject(self,obj):
		if obj.is_Group:
			return GROUP
		if obj.is_Bezier:
			return BEZIER
		if obj.is_Ellipse:
			return ELLIPSE
		if obj.is_Group:
			return RECTANGLE
		if obj.is_SimpleText:
			return SIMPLE_TEXT
		if obj.is_Image:
			return IMAGE
		return UNKNOWN_OBJ

PanelList=[PagePanel, ResizePanel, GuidesPanel, RotatePanel, 
		   FlipPanel, UnitPanel, GroupPanel, CombinePanel, ToCurvePanel]