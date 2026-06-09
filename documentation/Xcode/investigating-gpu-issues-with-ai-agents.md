# Investigating GPU issues with AI agents

**Framework**: Xcode

Find the root cause of an issue in a large GPU trace by handing the trace to an AI agent for autonomous investigation.

#### Overview

To help you investigate issues in GPU traces, the `gpudebug` command-line tool provides a text-based, self-discoverable interface that you can use programmatically, making it well-suited for AI agents.

Each row in the `list` command’s output shows node names and available actions, and the `go` command prints the destination’s children. An agent can explore an unfamiliar trace by following the actions each node advertises — without requiring any prior knowledge of the trace structure.

> 💡 **Tip**: For AI agents, point them at `man gpudebug` and a `.gputrace` file. That’s all they need to start investigating autonomously.

#### Reuse a Session for Multiple Commands

For any investigation involving more than one command, create a session once and reuse it. Trace loading and replayer startup can take seconds to minutes depending on the size of the trace; reusing a session avoids paying that cost on every invocation:

```shell
% gpudebug -t trace.gputrace -c "list"
Session 412 created.
...
% gpudebug -s 412 -c "go commands/cb0/re0/draw0" -c "info pipeline"
% gpudebug -s 412 -c "fetch color0"
% gpudebug -s 412 -c "next" -c "fetch color0"
% gpudebug --terminate 412
```

Each `-s` invocation reuses the already-loaded trace and replayer instantly.

#### Run One Off Queries with Oneshot

For an isolated single-command query where session management is a burden, use `--oneshot`. The option creates a session, runs the commands, and terminates, but it pays the full trace load cost on every invocation:

```shell
% gpudebug --oneshot -t trace.gputrace -c "go commands/cb0/re0/draw0" -c "info pipeline"
```

For the full command reference, see the `gpudebug(1)` manual page (`man gpudebug`).

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
- [Debugging with interactive command-line tools](debugging-with-interactive-command-line-tools.md)
  Investigate rendering issues in GPU traces without leaving the Terminal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/investigating-gpu-issues-with-ai-agents)*