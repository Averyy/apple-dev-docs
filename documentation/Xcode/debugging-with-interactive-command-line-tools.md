# Debugging with interactive command-line tools

**Framework**: Xcode

Investigate rendering issues in GPU traces without leaving the Terminal.

#### Overview

When a draw call produces incorrect output, like a missing shadow, a black surface, a flickering artifact, and so on, you need to navigate hundreds of API calls, inspect pipeline state, and examine resources to find the root cause. The `gpudebug` command lets you do this interactively from the command line, or as part of a scripted workflow.

This article walks through a complete debugging session, from opening a trace to identifying the source of a visual artifact. For the full command reference, run `man gpudebug`.

#### Open the Trace

Start `gpudebug` with the path to the trace file. You get a session number and an interactive prompt:

```shell
% gpudebug -t /path/to/Scene.gputrace
Session 412 created.
gpudebug — GPU Debugger (v1.0)
Trace:    /path/to/Scene.gputrace
Device:   Apple M4 Max
Summary:  3 command buffers, 18 encoders, 412 draw calls
Replayer ready.
gpudebug> 
```

The `REPL` is ready immediately, but the replayer loads in the background. You can use the `list` and `go` commands to navigate the trace structure while it connects; commands that need the live replay, such as `info pipeline` and `fetch`, block until the replayer is ready. For more information about the replayer, see [`Replaying a GPU trace file`](replaying-a-gpu-trace-file.md).

#### Find the Problematic Pass

Navigate the tree directly. The root has four children: `commands`, `performance`, `api_calls`, and `resources`. Start with the command buffers:

```shell
gpudebug> go commands/cb1/re0
Name     Label                                Summary                                 Actions
───────  ───────────────────────────────────  ──────────────────────────────────────  ───────────
color0   "CAMetalLayer Display Drawable (3)"  @tex18                                  info, fetch
color1   "Albedo + Shadow GBuffer"            @tex12 1536x1536 RGBA8Unorm_sRGB        info, fetch
depth    "MTKView Depth Stencil"              @tex15 1536x1536 Depth32Float_Stencil8  info, fetch
grp0     "Draw G-Buffer"                      8 draws                                          go
grp1     "Draw Directional Light"             1 draw                                           go
grp2     "Draw Light Mask"                    1 draw                                           go
grp3     "Draw Point Lights"                  1 draw                                           go
(7 items)
```

Navigate into the G-Buffer pass where the artifact appears:

```shell
gpudebug> go grp0/draw6
Name         Label                                Summary                                 Actions
───────────  ───────────────────────────────────  ──────────────────────────────────────  ───────────
pipeline     "G-buffer Creation"                  @rps0                                          info
vertex       "gbuffer_vertex"                     3 buffers                                        go
fragment     "gbuffer_fragment"                   1 buffer, 4 textures                             go
color0       "CAMetalLayer Display Drawable (3)"  @tex18                                  info, fetch
depth        "MTKView Depth Stencil"              @tex15 1536x1536 Depth32Float_Stencil8  info, fetch
indexBuffer  "MDL_OBJ-Indices"                    @buf4                                   info, fetch
(6 items)

Links:
  :a   /api_calls/api45
```

#### Inspect the Pipeline

When a draw produces incorrect output, start by inspecting its pipeline state. Run the `info` command on the pipeline node to print the entry points, color attachment formats, and vertex layout:

```shell
gpudebug commands/cb1/re0/grp0/draw6> info pipeline
label:  G-buffer Creation
name:   rps0

-- Entry Points --
vertex:    gbuffer_vertex (lib0 "MTLLibrary 1")
fragment:  gbuffer_fragment (lib0 "MTLLibrary 1")

-- Color Attachments --
  color0:  BGRA8Unorm_sRGB  (opaque)
  color1:  RGBA8Unorm_sRGB  (opaque)

-- Vertex Layout --
  buffer 0 (stride=12, perVertex):
    attr0   Float3  @0
  buffer 1 (stride=32, perVertex):
    attr1   Float2  @0
    attr2   Half4   @8
    attr3   Half4   @16
    attr4   Half4   @24
```

Draw calls also show encoder state (cull mode, winding order, depth-stencil state) so you can see the full render configuration at the point of the draw without navigating elsewhere:

```shell
gpudebug commands/cb1/re0/grp0/draw6> info
-[MTLRenderCommandEncoder drawIndexedPrimitives:indexCount:indexType:indexBuffer:indexBufferOffset:]
  primitiveType:      Triangle
  indexCount:         61266
  indexType:          UInt32
  indexBuffer:        @buf4 "MDL_OBJ-Indices"
  indexBufferOffset:  0

-- Encoder State --
Cull mode             Back
Front facing winding  Clockwise
Stencil front ref     128
Stencil back ref      128
Depth stencil state   @dss0 "G-buffer Creation (2)"
```

#### Fetch Attachments to See the Output

To see what a draw actually rendered, fetch its color attachment as a PNG file:

```shell
gpudebug commands/cb1/re0/grp0/draw6> fetch color0
Fetched .../commands_cb1_re0_grp0_draw6_color0.png (1.8 MiB)
```

To verify that this draw is the culprit, step backward and fetch the previous draw’s color attachment. If the previous draw renders correctly, the regression is in this draw’s setup, like its pipeline state, attachments, or shader inputs:

```shell
gpudebug commands/cb1/re0/grp0/draw6> prev
gpudebug commands/cb1/re0/grp0/draw5> fetch color0
```

#### Examine Shader Bindings

If the pipeline state and attachment look correct, the next suspect is the data the shaders received. Navigate into the `vertex` or `fragment` node to list the bound buffers and textures:

```shell
gpudebug commands/cb1/re0/grp0/draw6> go vertex
Name    Label                 Summary          Actions
──────  ────────────────────  ───────────────  ───────────
buf[0]  "MTLBuffer 8"         @buf7 252 KiB    info, fetch
buf[1]  "MTLBuffer 9"         @buf8 673 KiB    info, fetch
buf[2]  "LightPositions (2)"  @buf2 640 bytes  info, fetch
(3 items)
```

#### Browse Api Calls

The `api_calls` subtree provides a flat, chronological list of every Metal API call with inline argument values:

```shell
gpudebug> go api_calls
Name   Result  API Call                                                         Actions
─────  ──────  ───────────────────────────────────────────────────────────────  ────────
api0           [MTLLayer nextDrawable]                                              info
api1           [@cq0 commandBuffer]                                                 info
api2           [MTLCommandBuffer setLabel:"Shadow commands"]                        info
api3           [MTLCommandBuffer renderCommandEncoderWithDescriptor:<descriptor>]   info
api4           [MTLRenderCommandEncoder setLabel:"Shadow Map Pass"]                 info
api5           [MTLRenderCommandEncoder setRenderPipelineState:@rps4]               info
(showing 5 of 116 — use list N-M or list --all for more)
```

Draw, dispatch, and blit calls have bidirectional links. Use `go :d` from an API call to jump to its draw node, or `go :a` from a draw to find its API call.

#### Device Selection and Sessions

By default `gpudebug` replays on the local GPU. To target a remote device:

```shell
% gpudebug --list-devices
ID     Name       Model       OS
─────  ─────────  ──────────  ──────────
local  my-mac     Mac15,9     macOS 26.2
0      my-iphone  iPhone17,4  iOS 27.0

% gpudebug -t trace.gputrace -d 0
```

> ❗ **Important**: Remote device discovery requires Xcode to be running. Xcode provides the device browser service that `gpudebug` connects to.

Sessions persist after you disconnect. Use the `exit` command to detach and `gpudebug -s <id>` to reconnect later. Use `exit --terminate` to end a session when you’re done.

## See Also

- [Capturing a Metal workload in Xcode](capturing-a-metal-workload-in-xcode.md)
  Analyze your app’s performance by configuring your project to use the Metal debugger.
- [Capturing a Metal workload programmatically](capturing-a-metal-workload-programmatically.md)
  Analyze your app’s performance by invoking Metal’s frame capture.
- [Replaying a GPU trace file](replaying-a-gpu-trace-file.md)
  Debug and profile your app’s performance using a GPU trace file in the Metal debugger.
- [Investigating visual artifacts](investigating-visual-artifacts.md)
  Discover, diagnose, and fix visual artifacts in your app with the Metal debugger.
- [Optimizing GPU performance](optimizing-gpu-performance.md)
  Find and address performance bottlenecks using the Metal debugger.
- [Investigating GPU issues with AI agents](investigating-gpu-issues-with-ai-agents.md)
  Find the root cause of an issue in a large GPU trace by handing the trace to an AI agent for autonomous investigation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/debugging-with-interactive-command-line-tools)*