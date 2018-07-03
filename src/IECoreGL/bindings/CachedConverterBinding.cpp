//////////////////////////////////////////////////////////////////////////
//
//  Copyright (c) 2012-2013, Image Engine Design Inc. All rights reserved.
//
//  Redistribution and use in source and binary forms, with or without
//  modification, are permitted provided that the following conditions are
//  met:
//
//     * Redistributions of source code must retain the above copyright
//       notice, this list of conditions and the following disclaimer.
//
//     * Redistributions in binary form must reproduce the above copyright
//       notice, this list of conditions and the following disclaimer in the
//       documentation and/or other materials provided with the distribution.
//
//     * Neither the name of Image Engine Design nor the names of any
//       other contributors to this software may be used to endorse or
//       promote products derived from this software without specific prior
//       written permission.
//
//  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
//  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
//  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
//  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
//  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
//  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
//  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
//  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
//  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
//  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
//  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
//////////////////////////////////////////////////////////////////////////

#include "boost/python.hpp"

#include "IECoreGL/bindings/CachedConverterBinding.h"

#include "IECoreGL/CachedConverter.h"

#include "IECorePython/RefCountedBinding.h"
#include "IECorePython/ScopedGILRelease.h"

using namespace boost::python;
using namespace IECoreGL;

namespace
{

IECore::RunTimeTypedPtr convert( CachedConverter &c, IECore::ObjectPtr o )
{
	IECorePython::ScopedGILRelease gilRelease;
	return boost::const_pointer_cast<IECore::RunTimeTyped>( c.convert( o.get() ) );
}

void clearUnused( CachedConverter &c )
{
	IECorePython::ScopedGILRelease gilRelease;
	c.clearUnused();
}

} // namespace

void IECoreGL::bindCachedConverter()
{
	IECorePython::RefCountedClass<CachedConverter, IECore::RefCounted>( "CachedConverter" )
		.def( init<size_t>() )
		.def( "convert", &convert )
		.def( "getMaxMemory", &CachedConverter::getMaxMemory )
		.def( "setMaxMemory", &CachedConverter::setMaxMemory )
		.def( "clearUnused", &clearUnused )
		.def( "defaultCachedConverter", &CachedConverter::defaultCachedConverter, return_value_policy<IECorePython::CastToIntrusivePtr>() )
		.staticmethod( "defaultCachedConverter" )
	;
}
