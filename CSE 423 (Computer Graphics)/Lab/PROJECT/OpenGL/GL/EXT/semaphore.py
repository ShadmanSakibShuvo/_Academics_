'''OpenGL extension EXT.semaphore

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.semaphore to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/semaphore.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.semaphore import *
from OpenGL.raw.GL.EXT.semaphore import _EXTENSION_NAME

def glInitSemaphoreEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

# INPUT glGetUnsignedBytevEXT.data size not checked against 'pname'
glGetUnsignedBytevEXT=wrapper.wrapper(glGetUnsignedBytevEXT).setInputArraySize(
    'data', None
)
# INPUT glGetUnsignedBytei_vEXT.data size not checked against 'target'
glGetUnsignedBytei_vEXT=wrapper.wrapper(glGetUnsignedBytei_vEXT).setInputArraySize(
    'data', None
)
# INPUT glGenSemaphoresEXT.semaphores size not checked against n
glGenSemaphoresEXT=wrapper.wrapper(glGenSemaphoresEXT).setInputArraySize(
    'semaphores', None
)
# INPUT glDeleteSemaphoresEXT.semaphores size not checked against n
glDeleteSemaphoresEXT=wrapper.wrapper(glDeleteSemaphoresEXT).setInputArraySize(
    'semaphores', None
)
# INPUT glWaitSemaphoreEXT.buffers size not checked against 'numBufferBarriers'
# INPUT glWaitSemaphoreEXT.srcLayouts size not checked against 'numTextureBarriers'
# INPUT glWaitSemaphoreEXT.textures size not checked against 'numTextureBarriers'
glWaitSemaphoreEXT=wrapper.wrapper(glWaitSemaphoreEXT).setInputArraySize(
    'buffers', None
).setInputArraySize(
    'srcLayouts', None
).setInputArraySize(
    'textures', None
)
# INPUT glSignalSemaphoreEXT.buffers size not checked against 'numBufferBarriers'
# INPUT glSignalSemaphoreEXT.dstLayouts size not checked against 'numTextureBarriers'
# INPUT glSignalSemaphoreEXT.textures size not checked against 'numTextureBarriers'
glSignalSemaphoreEXT=wrapper.wrapper(glSignalSemaphoreEXT).setInputArraySize(
    'buffers', None
).setInputArraySize(
    'dstLayouts', None
).setInputArraySize(
    'textures', None
)
### END AUTOGENERATED SECTION