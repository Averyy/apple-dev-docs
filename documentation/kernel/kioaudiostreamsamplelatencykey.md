# kIOAudioStreamSampleLatencyKey

**Framework**: Kernel  
**Kind**: macro  
**Role**: Macro

The key in the IORegistry for the IOAudioStream output sample latency key

**Availability**:
- macOS 10.3+

## Declaration

```c
#define kIOAudioStreamSampleLatencyKey
```

#### Discussion

Tells the HAL how much latency is on a particular stream. If two streams on the same engine have different latencies (e.g. one is analog, one is digital), then set this property on both streams to inform the HAL of the latency differences. Alternately, you can set the engine latency, and just include the latency additional to that for the particular stream. The HAL will add the engine and stream latency numbers together to get the total latency.


---

*[View on Apple Developer](https://developer.apple.com/documentation/kernel/kioaudiostreamsamplelatencykey)*