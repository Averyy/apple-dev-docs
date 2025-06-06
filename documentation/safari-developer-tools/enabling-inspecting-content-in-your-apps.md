# Enabling inspecting content in your apps

**Framework**: Safari Developer Features

Enable the inspection of webpages and JavaScript in apps you develop when inspected from a connected Mac.

#### Overview

Web content and JavaScript is used for various purposes in apps, from providing UI from a webpage to enabling apps to be scriptable.

##### When Should I Consider Making Content Inspectable

A common situation in which you may want the content of `WKWebView` to be inspectable is in an in-app web browser. The browser shows ordinary web content that would be inspectable when loaded in Safari. It can be beneficial both for the app developer, as well as web authors, to be able to inspect content in these views, as the size of the view may not match that of Safari’s, or the app developer may be injecting script into the view to provide integration with their app.

Web content is often dynamic, delivered by a server—not in the app—and easily changed over time. Unfortunately, not all issues can or will get debugged by folks with access to a developer-provisioned copy of your app.

`JSContext` can also enable scripting in an app whereby the customer provides the scripts to augment the app. Without the ability for a release version of your app to adopt inspectability, your customers may have no way to debug the scripts they have written. It makes it harder for customers to use this functionality of your app.

#### Enabling Inspection

Across all platforms supporting `WKWebView` or `JSContext`, a new property is available called `isInspectable` (`inspectable` in Objective-C). It defaults to `false`, and you can set it to `true` to opt-in to content being inspectable. This decision is made for each individual `WKWebView` and `JSContext` to prevent unintentionally making it enabled for a view or context you don’t intend to be inspectable. So, for example, to make a `WKWebView` `inspectable`, you would:

```swift
let webConfiguration = WKWebViewConfiguration()
let webView = WKWebView(frame: .zero, configuration: webConfiguration)
webView.isInspectable = true
```

```objc
WKWebViewConfiguration *webConfiguration = [WKWebViewConfiguration new];
WKWebView *webView = [[WKWebView alloc] initWithFrame:CGRectZero configuration:webConfiguration];
webView.inspectable = YES;
```

For `JSContext`, matching API is available, with the addition of C API for developers using `JSGlobalContextRef`:

```swift
let jsContext = JSContext()
jsContext?.isInspectable = true
```

```objc
JSContext *jsContext = [JSContext new];
jsContext.inspectable = YES;
```

```c
JSGlobalContextRef jsContextRef = JSGlobalContextCreate(NULL);
JSGlobalContextSetInspectable(jsContextRef, true);
```

The inspectable property can be changed at any point during the lifetime of your WKWebView or JSContext. Disabling inspection while Web Inspector actively inspects the content will automatically close Web Inspector, and no further information about the content will be available.

Once you’ve enabled inspection for your app, you can inspect it from Safari’s Develop menu in the submenu for either your current computer or an attached device.

#### Provide Readable Names for Inspectable Jscontexts

Unlike `WKWebView`, which automatically gets a name based on the page currently loaded in the view, every `JSContext` with `inspectable` enabled will be listed as  in Safari’s  menu. Provide a unique, human-readable name for each inspectable `JSContext` to make it easier for you and your customers to determine what the `JSContext` represents. For example, if your app runs different pieces of JavaScript on behalf of the user, you should give each `JSContext` a name based on what runs inside the context.

API is available to set the user-visible `name` of a `JSContext`:

```swift
let jsContext = JSContext()
jsContext?.name = "Context name"
```

```objc
JSContext *jsContext = [JSContext new];
jsContext.name = @"Context name";
```

```c
JSGlobalContextRef jsContextRef = JSGlobalContextCreate(NULL);
JSGlobalContextSetName(jsContextRef, JSStringCreateWithUTF8CString("Context name"));
```

#### Working with Older Versions of Macos and Ios

For apps linked against an SDK before macOS 13.3 and iOS 16.4, `WKWebView`s and `JSContext`s will continue to follow the previous behavior of always being inspectable when built for debugging from Xcode.

Apps that support older versions of macOS and iOS while linked against the most recent SDK will not get the previous behavior of all content being inspectable in debug builds to avoid confusion about what will and will not be inspectable by customers. Apps targeting older OS versions but linking against the new SDK can use this new API conditionally on OS versions that support it. To conditionally guard usage of the API:

```swift
if #available(macOS 13.3, iOS 16.4, tvOS 16.4, *) {
    webView.isInspectable = true
}
```

```objc
if (@available(macOS 13.3, iOS 16.4, tvOS 16.4, *))
    webView.inspectable = YES;
```

[`Learn more about guarding usage of new API based on availability.`](https://developer.apple.comhttps://developer.apple.com/documentation/swift/marking-api-availability-in-objective-c)

## See Also

- [Inspecting Safari on macOS](inspecting-safari-macos.md)
  Inspect webpages, Service Workers, and extensions in Safari on macOS.
- [Inspecting iOS and iPadOS](inspecting-ios.md)
  Inspect webpages, Service Workers, Home Screen web apps, extensions, and content inside apps on iOS and iPadOS devices and simulators from a connected Mac.
- [Inspecting visionOS](inspecting-visionos.md)
  Inspect webpages, service workers, extensions, and content inside apps in visionOS from a Mac on the same network.
- [Inspecting tvOS](inspecting-tvos.md)
  Inspect JavaScript and TVML content on tvOS from a Mac on the same network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safari-developer-tools/enabling-inspecting-content-in-your-apps)*