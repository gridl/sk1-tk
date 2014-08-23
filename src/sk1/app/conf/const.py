# -*- coding: utf-8 -*-

# Copyright (C) 2003-2006 by Igor E. Novikov
# Copyright (C) 1997, 1998, 1999 by Bernhard Herzog
#
# This library is covered by GNU Library General Public License.
# For more info see COPYRIGHTS file in sK1 root directory.

#
#	Constants...
#



CAIRO_ANTIALIAS_DEFAULT  = 0
CAIRO_ANTIALIAS_NONE     = 1
CAIRO_ANTIALIAS_GRAY     = 2
CAIRO_ANTIALIAS_SUBPIXEL = 3

CAIRO_FILTER_FAST        = 0
CAIRO_FILTER_GOOD        = 1
CAIRO_FILTER_BEST        = 2
CAIRO_FILTER_NEAREST     = 3
CAIRO_FILTER_BILINEAR    = 4

CAIRO_OPERATOR_CLEAR     = 0
CAIRO_OPERATOR_SOURCE    = 1
CAIRO_OPERATOR_OVER      = 2
CAIRO_OPERATOR_IN        = 3
CAIRO_OPERATOR_OUT       = 4
CAIRO_OPERATOR_ATOP      = 5
CAIRO_OPERATOR_DEST      = 6
CAIRO_OPERATOR_DEST_OVER = 7
CAIRO_OPERATOR_DEST_IN   = 8
CAIRO_OPERATOR_DEST_OUT  = 9
CAIRO_OPERATOR_DEST_ATOP = 10
CAIRO_OPERATOR_XOR       = 11
CAIRO_OPERATOR_ADD       = 12
CAIRO_OPERATOR_SATURATE  = 13


#
#	Types of handles
#

# physical
# for rect handles: filled == handle_id & 1

Handle_OpenRect		= 0
Handle_FilledRect	= 1
Handle_SmallOpenRect	= 2
Handle_SmallFilledRect	= 3

Handle_OpenCircle	= 4
Handle_FilledCircle	= 5
Handle_SmallOpenCircle	= 6
Handle_SmallFilledCircle = 7

Handle_SmallOpenRectList = 8

Handle_Line		= 9
Handle_Pixmap		= 10
Handle_Caret		= 11
Handle_PathText         = 12

# logical	XXX should these be moved to config.py?
Handle			= Handle_FilledRect
HandleNode		= Handle_OpenRect
HandleSelectedNode	= Handle_FilledRect
HandleControlPoint	= Handle_SmallFilledRect
HandleLine		= Handle_Line
HandleCurvePoint        = Handle_FilledCircle

#
#
#

# The corners of the unit rectangle
corners = [(0, 0), (1, 0), (1, 1), (0, 1)]


#
#	Standard channel names
#

# common
CHANGED = 'CHANGED'
DOCUMENT = 'DOCUMENT'
MODE = 'MODE'
SELECTION = 'SELECTION'

# dialogs
CLOSED = 'CLOSED'

# TKExt
COMMAND = 'COMMAND'
# also uses SELECTION

# APPLICATION
CLIPBOARD = 'CLIPBOARD'
ADD_TO_SPECIAL_MENU = 'ADD_TO_SPECIAL_MENU'

# Global
INITIALIZE = 'INITIALIZE'
APP_INITIALIZED = 'APP_INITIALIZED'
INIT_READLINE = 'INIT_READLINE'
MOVING = 0

# CANVAS
STATE = 'STATE'
UNDO = 'UNDO'
VIEW = 'VIEW'
POSITION = 'POSITION'
CURRENTINFO = 'CURRENTINFO'

# DOCUMENT
EDITED = 'EDITED'
GRID = 'GRID'
LAYER = 'LAYER'
LAYER_STATE = 'LAYER_STATE';	LAYER_ORDER = 'LAYER_ORDER'
LAYER_COLOR = 'LAYER_COLOR';	LAYER_ACTIVE = 'LAYER_ACTIVE'
LAYOUT = 'LAYOUT'
REDRAW = 'REDRAW'
STYLE = 'STYLE'
UNDO = 'UNDO'
GUIDE_LINES = 'GUIDE_LINES'
PAGE = 'PAGE'


# graphics object
#TRANSFORMED = 'TRANSFORMED'

# command
UPDATE = 'update'

# palette
COLOR1 = 'color1'
COLOR2 = 'color2'

# Drop types
DROP_COLOR = 'COLOR'


#
#       Scripting Access
#

SCRIPT_UNDO = 'SCRIPT_UNDO'
SCRIPT_GET = 'SCRIPT_GET'
SCRIPT_OBJECT = 'SCRIPT_OBJECT'
SCRIPT_OBJECTLIST = 'SCRIPT_OBJECTLIST'

#
#	constants for selections
#

# the same as in curveobject.c
SelectSet = 0
SelectAdd = 1
SelectSubtract = 2
SelectSubobjects = 3
SelectDrag = 4

SelectGuide = 5

# Arc modes. bezier_obj.approx_arc uses these
ArcArc = 0
ArcChord = 1
ArcPieSlice = 2

#
#	X specific stuff
#

from app.X11 import X

ShiftMask = X.ShiftMask
LockMask = X.LockMask
ControlMask = X.ControlMask
Mod1Mask = X.Mod1Mask
Mod2Mask = X.Mod2Mask
Mod3Mask = X.Mod3Mask
Mod4Mask = X.Mod4Mask
Mod5Mask = X.Mod5Mask
MetaMask = Mod1Mask

Button1Mask = X.Button1Mask
Button2Mask = X.Button2Mask
Button3Mask = X.Button3Mask
Button4Mask = X.Button4Mask
Button5Mask = X.Button5Mask
AllButtonsMask = Button1Mask | Button2Mask | Button3Mask

Button1 = X.Button1
Button2 = X.Button2
Button3 = X.Button3
Button4 = X.Button4
Button5 = X.Button5

ContextButton	= Button3
ContextButtonMask = Button3Mask

AllowedModifierMask = ShiftMask | ControlMask | MetaMask
ConstraintMask = ControlMask
AlternateMask = ShiftMask

AddSelectionMask = ShiftMask
SubtractSelectionMask = MetaMask

SubobjectSelectionMask = ControlMask 

#
#	Line Styles
#

JoinMiter	= X.JoinMiter
JoinRound	= X.JoinRound
JoinBevel	= X.JoinBevel
CapButt		= X.CapButt
CapRound	= X.CapRound
CapProjecting	= X.CapProjecting


# cursors

CurStd		= 'top_left_arrow'# is replaced by custom cursor in uimanager
CurHandle	= 'crosshair' # is replaced by custom cursor in uimanager
CurPick		= 'hand2' # is replaced by custom cursor in uimanager
CurMove		= 'hand2'# is replaced by custom cursor in uimanager
#---------Tool cursors-------------
CurCreate	= 'crosshair'# is replaced by custom cursor in uimanager
CurCreateRect	= 'crosshair'# is replaced by custom cursor in uimanager 
CurCreateEllipse= 'crosshair'# is replaced by custom cursor in uimanager 
CurCreatePolyline= 'crosshair'# is replaced by custom cursor in uimanager
CurCreateBezier= 'crosshair'# is replaced by custom cursor in uimanager
#----------------------------------
CurPlace	= 'crosshair'	# is replaced by custom cursor in uimanager
CurHGuide       = 'sb_v_double_arrow' # is replaced by custom cursor in uimanager
CurVGuide       = 'sb_h_double_arrow' # is replaced by custom cursor in uimanager
CurZoom		= 'plus'	# is replaced by custom cursor in uimanager
CurCopy		= 'plus'	# is replaced by custom cursor in uimanager

CurEdit     = 'left_ptr'	# is replaced by custom cursor in uimanager
CurText     = 'xterm'	# is replaced by custom cursor in uimanager

#-----------Should be system defined-------------
CurHResize  = 'sb_h_double_arrow'
CurVResize  = 'sb_v_double_arrow'

#-----------Obsolete or unused-----------
CurUp       = 'based_arrow_up'
CurUpDown   = 'sb_v_double_arrow'
CurDown     = 'based_arrow_down'
CurDragColor	= 'spraycan'
CurTurn		= 'exchange'
CurHelp		= 'question_arrow'
CurWait		= 'watch'


#
# Text Alignment
#
ALIGN_BASE = 0
ALIGN_CENTER = 1
ALIGN_TOP = 2
ALIGN_BOTTOM = 3

ALIGN_LEFT = 0
ALIGN_CENTER = 1
ALIGN_RIGHT = 2