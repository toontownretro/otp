"""
GraphicsDebugInfo
Author: Loonatic
Date: 11 December 2022

Print out hardware and engine information from GraphicsStateGuardian and GraphicsPipe

Also includes pointers to engine-level rendering modules such as the GSG (GraphicsStateGuardian) and
PreparedGraphicsObjects
"""

"""
from otp.debug import GraphicsDebugInfo as gdi
gdi.printGraphicsDebugInfo()
"""

gsg = base.win.gsg  # type: GraphicsStateGuardian
gp = gsg.pipe  # type: GraphicsPipe
obj = gsg.prepared_objects  # type: PreparedGraphicsObjects


def getGPUInfo():
    """
    Grabs GPU hardware information
    """
    GPUInfo = {
        "Driver Renderer": gsg.getDriverRenderer(),
        "Driver Shader Version (Major)": gsg.getDriverShaderVersionMajor(),
        "Driver Shader Version (Minor)": gsg.getDriverShaderVersionMinor(),
        "Driver Vendor": gsg.getDriverVendor(),
        "Driver Version": gsg.getDriverVersion(),
        "Driver Version (Major)": gsg.getDriverVersionMajor(),
        "Driver Version (Minor)": gsg.getDriverVersionMinor(),
        "Graphics Memory Limit (raw)": obj.getGraphicsMemoryLimit(),
        # "Graphics Memory Limit (MB)": obj.getGraphicsMemoryLimit() / 1048576,  # relevant to GPUInfo
    }
    return GPUInfo


def printGPUInfo():
    """
    Prints GPU hardware information from calling getGPUInfo
    """
    GPUInfo = getGPUInfo()
    for k, v in GPUInfo.items():
        print(k, v)


def getDisplayInfo():
    gp.lookupCpuData()
    DisplayInfo = {
        "Known Display Width": gp.getDisplayWidth(),
        "Known Display Height": gp.getDisplayHeight(),
        "Display Information": gp.getDisplayInformation(),  # type: DisplayInformation
        "Display Zoom": gp.getDisplayZoom(),  # type: float
        "Interface Name": gp.getInterfaceName(),  # type: str
        "Supported Types": gp.getSupportedTypes(),  # type: int
        "Valid": gp.isValid()  # type: bool
    }
    return DisplayInfo


def printDisplayInfo():
    DisplayInfo = getDisplayInfo()
    for k, v in DisplayInfo.items():
        print(k, v)


def checkSupported():
    GSGSupported = {
        "Basic Shaders (arbfp1+arbvp1)": gsg.getSupportsBasicShaders(),
        "Buffer Textures": gsg.getSupportsBufferTexture(),
        # getSupportsCgProfile
        "Compressed Textures": gsg.getSupportsCompressedTexture(),
        "Compute Shaders": gsg.getSupportsComputeShaders(),
        "Depth Stencil": gsg.getSupportsDepthStencil(),
        "Depth Texture": gsg.getSupportsDepthTexture(),
        "Dual Source Blending": gsg.getSupportsDualSourceBlending(),
        "Mipmaps": gsg.getSupportsGenerateMipmap(),
        "Geometry Instancing": gsg.getSupportsGeometryInstancing(),  # Render multiple copies of a model
        "Geometry Shaders": gsg.getSupportsGeometryShaders(),
        "GLSL Shaders": gsg.getSupportsGlsl(),  # GLSL Shader support
        "Indirect Draw Calls": gsg.getSupportsIndirectDraw(),  # Info comes from a buffer
        "Luminance Textures": gsg.getSupportsLuminanceTexture(),
        "Occlusion Queries": gsg.getSupportsOcclusionQuery(),
        "Sampler Objects": gsg.getSupportsSamplerObjects(),
        "Stencil Buffers": gsg.getSupportsStencil(),
        "Tessellation Shaders": gsg.getSupportsTessellationShaders(),
        "Non-pow2 Textures": gsg.getSupportsTexNonPow2(),
        "Texture Combine (TextureStage::M_combine)": gsg.getSupportsTextureCombine(),
        # If this is false, you must limit yourself to using the simpler blend modes.
        "Texture dot3 (TextureStage::CM_dot3_rgb)": gsg.getSupportsTextureDot3(),
        "Last saved Texture Stages (TextureStage::CS_last_saved_result)": gsg.getSupportsTextureSavedResult(),
        "Timer Queries": gsg.getSupportsTimerQuery(),
        "Two-Sided Stencil": gsg.getSupportsTwoSidedStencil(),
    }
    return GSGSupported


def printSupported():
    GSGSupported = checkSupported()
    for k, v in GSGSupported.items():
        print(k, v)


def getGSGInfo():
    GSGInfo = {
        "Default GSG": gsg.getDefaultGsg(),  # type: GraphicsStateGuardianBase
        "Effective Incomplete Render": gsg.getEffectiveIncompleteRender(),
        "Incomplete Render": gsg.getIncompleteRender(),
        "Graphics State Guardian Count": gsg.getNumGsgs(),  # type: int
        "Graphic State Guardians": gsg.getGsgs(),  # type: list
        "Maximum Texture Dimension": gsg.getMaxTextureDimension(),  # type: int
        "Maximum Vertices per Array": gsg.getMaxVerticesPerArray(),  # type: int
        "Maximum Vertices per Primitive": gsg.getMaxVerticesPerPrimitive(),  # type: int
        "Supported Geom Rendering": gsg.getSupportedGeomRendering(),
        "Supports HLSL": gsg.getSupportsHlsl(),
        "Supports Multisampling": gsg.getSupportsMultisample(),
        "Supports Shadow Filter": gsg.getSupportsShadowFilter(),
        "Supports sRGB Textures": gsg.getSupportsTextureSrgb(),
        "Prefers Triangle Strips": gsg.prefersTriangleStrips()
    }
    return GSGInfo


def printGSGInfo():
    GSGInfo = getGSGInfo()
    for k, v in GSGInfo.items():
        print(k, v)


def checkStatus():
    GSGStatus = {
        "Active": gsg.isActive(),
        "Initialized/Valid": gsg.isValid(),
        "Hardware Acceleration": gsg.isHardware(),
        "Allowing Incomplete Rendering": gsg.getIncompleteRender(),
        "Texture Quality Override": gsg.getTextureQualityOverride(),  # type: QualityLevel
        "Coordinate System": gsg.getCoordinateSystem(),  # type: CoordinateSystem
        "Internal Coordinate System": gsg.getInternalCoordinateSystem(),  # type: CoordinateSystem
        "Marked, Needs Reset": gsg.needsReset(),
    }
    return GSGStatus


def printStatus():
    GSGStatus = checkStatus()
    for k, v in GSGStatus.items():
        print(k, v)


def getPreparedObjects():
    """
    Prepared objects are currently being called for render
    """
    GSGPreparedObjects = {
        "All Objects": obj.getNumPrepared(),
        "Geoms": obj.getNumPreparedGeoms(),
        "Index Buffers": obj.getNumPreparedIndexBuffers(),
        "Samplers": obj.getNumPreparedSamplers(),
        "Shader Buffers": obj.getNumPreparedShaderBuffers(),
        "Shaders": obj.getNumPreparedShaders(),
        "Textures": obj.getNumPreparedTextures(),
        "Vertex Buffers": obj.getNumPreparedVertexBuffers(),
    }
    return GSGPreparedObjects


def printPreparedObjects():
    GSGPreparedObjects = getPreparedObjects()
    for k, v in GSGPreparedObjects.items():
        print(k, v)


def getQueuedObjects():
    """
    Queued objects are still in memory/cache but are not being called for
    """
    GSGQueuedObjects = {
        "All Objects": 0,
        "Geoms": 0,
        "Index Buffers": 0,
        "Samplers": 0,
        "Shader Buffers": 0,
        "Shaders": 0,
        "Textures": 0,
        "Vertex Buffers": 0,
    }
    return GSGQueuedObjects


# if we ever make a standalone camera debug module we can migrate this over there
def getDisplayRegionInfo():
    amt = base.win.getNumDisplayRegions()
    regions = []
    regionCams = []  # type: List[NodePath]
    regionLensIndex = []  # type: int
    regionWindow = []  # type: GraphicsOutput
    regionActive = []  # type: bool
    regionSort = []  # type: int
    regionPixelSize = []  # type: LVecBase2i
    for dr in range(amt):
        regions.append(dr)
        region = base.win.getDisplayRegion(dr)
        regionCams.append(region.getCamera())
        regionLensIndex.append(region.lens_index)
        regionWindow.append(region.getWindow())
        regionActive.append(region.isActive())
        regionSort.append(region.getSort())
        regionPixelSize.append(region.pixel_size)

    DisplayRegionInfo = {
        "Number of Display Regions": amt,
        "Display Regions": regions,
        "Region Camera": regionCams,
        "Region Lens": regionLensIndex,
        "Region Window": regionWindow,
        "Active Region": regionActive,
        "Sort Value": regionSort,
        "Pixel Size": regionPixelSize,
    }
    return DisplayRegionInfo


def printDisplayRegionInfo():
    DisplayRegionInfo = getDisplayRegionInfo()
    for k, v in DisplayRegionInfo.items():
        print(k, v)

def printGraphicsDebugInfo():
    """
    Prints out a ton of debug information related to the GPU, window, engine, etc.
    """
    print("==== GPUInfo ====")
    printGPUInfo()
    print("================")
    print("==== Display Info ====")
    printDisplayInfo()
    print("================")
    print("==== Display Region Info ====")
    printDisplayRegionInfo()
    print("================")
    print("==== Supported Info ====")
    printSupported()
    print("================")
    print("==== GSG Info ====")
    printGSGInfo()
    print("================")
    print("==== GSG Status ====")
    printStatus()
    print("================")
    print("==== GSG Prepared Objects ====")
    printPreparedObjects()
    print("================")
