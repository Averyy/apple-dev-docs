# ProExtensionHostSingleton()

**Framework**: Professional Video Applications  
**Kind**: func  
**Role**: Function

Returns the singleton proxy instance of the host object.

**Availability**:
- ProVideo Workflow Extensions 1.0+

## Declaration

```swift
func ProExtensionHostSingleton() -> (any NSObjectProtocol)?
```

```c
extern id<NSObject> ProExtensionHostSingleton();
```

## Mentions

- [Interacting with the Final Cut Pro Timeline](../Professional-Video-Applications/interacting-with-the-final-cut-pro-timeline.md)

#### Return Value

An object that represents the singleton proxy instance of the host object.

#### Discussion

The ProExtensionHost framework creates an instance of the proxy host object during workflow extension startup. The host object provides an initial access point for workflow extensions to interact with the Final Cut Pro timeline. Call this function to get the singleton instance of the proxy host object.

A workflow extension is expected to validate that the returned instance of the proxy host object conforms to the [`FCPXHost`](./fcpxhost.md) protocol. After accessing the host object, cast the object to `id<FCPXHost>` type to access its properties.

**Swift**:

```swift
host = ProExtensionHostSingleton() as? FCPXHost
```

**Objective-C**:

```objc
(id<NSObject>)singleton = ProExtensionHostSingleton();
id<FCPXHost> host = nil;

if ([singleton conformsToProtocol:@protocol(FCPXHost)])
    host = (id<FCPXHost>)singleton
```

## See Also

### FCPX Interactions
- [Interacting with the Final Cut Pro Timeline](../Professional-Video-Applications/interacting-with-the-final-cut-pro-timeline.md)
  Extend your workflows beyond media exchange by enabling a workflow extension to interact with the Final Cut Pro timeline.
- [protocol FCPXHost](./fcpxhost.md)
  A protocol that provides an interface to retrieve the Final Cut Pro timeline proxy objects and details of the host app.
- [class FCPXTimeline](./fcpxtimeline.md)
  An interface that has methods and properties to communicate and interact with the Final Cut Pro timeline.
- [protocol FCPXTimelineObserver](./fcpxtimelineobserver.md)
  An interface with optional methods implemented by observers of [`FCPXTimeline`](./fcpxtimeline.md) objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/proextensionhostsingleton())*