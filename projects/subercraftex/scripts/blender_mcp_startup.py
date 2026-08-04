# Run at every Blender launch via the com.subercraftex.blender-mcp LaunchAgent
# (see PROJECT.md's "Blender MCP" section for why this exists).
#
# The blender-mcp addon's own register() reads bpy.context.scene to decide
# which port to auto-start on, but that context isn't reliably available at
# the exact moment Blender auto-registers a previously-enabled addon on
# startup -- it can silently fall back to its hardcoded default (9876),
# which collides with the Fusion 360 add-in already listening there. This
# script re-asserts the correct state every launch instead of trusting that
# race to resolve correctly on its own: explicitly stop whatever may have
# auto-started, force the port to 9877 (kept clear of Fusion 360's 9876,
# see PROJECT.md), start the server, then persist that as the default so
# a plain launch (no script) also has the best chance of getting it right.

import bpy

ADDON_MODULE = "addon"
BLENDER_MCP_PORT = 9877

if ADDON_MODULE not in bpy.context.preferences.addons:
    bpy.ops.preferences.addon_enable(module=ADDON_MODULE)

try:
    bpy.ops.blendermcp.stop_server()
except Exception as e:
    print("blendermcp.stop_server (expected if nothing was running):", e)

scene = bpy.context.scene
scene.blendermcp_port = BLENDER_MCP_PORT
scene.blendermcp_auto_start_server = True

bpy.ops.blendermcp.start_server()
print(
    "BlenderMCP login startup: running =", scene.blendermcp_server_running,
    "port =", scene.blendermcp_port,
)

bpy.ops.wm.save_userpref()
bpy.ops.wm.save_homefile()
