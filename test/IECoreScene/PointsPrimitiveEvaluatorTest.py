##########################################################################
#
#  Copyright (c) 2010, Image Engine Design Inc. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#     * Neither the name of Image Engine Design nor the names of any
#       other contributors to this software may be used to endorse or
#       promote products derived from this software without specific prior
#       written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

from __future__ import with_statement

import unittest
import imath

import IECore
import IECoreScene

class PointsPrimitiveEvaluatorTest( unittest.TestCase ) :

	def testCreate( self ) :

		p = IECoreScene.PointsPrimitive( 5 )
		p["P"] = IECoreScene.PrimitiveVariable( IECoreScene.PrimitiveVariable.Interpolation.Vertex, IECore.V3fVectorData( [ imath.V3f( x ) for x in range( 0, 5 ) ] ) )

		e = IECoreScene.PrimitiveEvaluator.create( p )
		self.assertTrue( isinstance( e, IECoreScene.PointsPrimitiveEvaluator ) )
		self.assertEqual( e.primitive(), p )

	def testConstruct( self ) :

		p = IECoreScene.PointsPrimitive( 5 )
		p["P"] = IECoreScene.PrimitiveVariable( IECoreScene.PrimitiveVariable.Interpolation.Vertex, IECore.V3fVectorData( [ imath.V3f( x ) for x in range( 0, 5 ) ] ) )

		e = IECoreScene.PointsPrimitiveEvaluator( p )
		self.assertTrue( isinstance( e, IECoreScene.PointsPrimitiveEvaluator ) )
		self.assertEqual( e.primitive(), p )

	def testClosestPoint( self ) :

		p = IECoreScene.PointsPrimitive( 5 )
		p["P"] = IECoreScene.PrimitiveVariable( IECoreScene.PrimitiveVariable.Interpolation.Vertex, IECore.V3fVectorData( [ imath.V3f( x, 0, 0 ) for x in range( 0, 5 ) ] ) )
		p["Cs"] = IECoreScene.PrimitiveVariable( IECoreScene.PrimitiveVariable.Interpolation.Vertex, IECore.Color3fVectorData( [ imath.Color3f( r, 0, 0 ) for r in range( 5, 10 ) ] ) )
		p["names"] = IECoreScene.PrimitiveVariable( IECoreScene.PrimitiveVariable.Interpolation.Vertex, IECore.StringVectorData( [ "a", "b", "c", "d", "e" ] ) )

		e = IECoreScene.PointsPrimitiveEvaluator( p )
		r = e.createResult()

		s = e.closestPoint( imath.V3f( -1, -1, 0 ), r )
		self.assertEqual( s, True )
		self.assertEqual( r.pointIndex(), 0 )
		self.assertEqual( r.point(), imath.V3f( 0 ) )
		self.assertEqual( r.colorPrimVar( p["Cs"] ), imath.Color3f( 5, 0, 0 ) )
		self.assertEqual( r.stringPrimVar( p["names"] ), "a" )

if __name__ == "__main__":
	unittest.main()

