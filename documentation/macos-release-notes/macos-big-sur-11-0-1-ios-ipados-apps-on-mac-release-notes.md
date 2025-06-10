# macOS Big Sur 11.0.1 iOS & iPadOS Apps on Mac Release Notes

**Framework**: macOS Release Notes

Considerations for running iPhone and iPad apps on Macs with Apple silicon.

#### Overview

Macs with Apple silicon can run many iPad and iPhone apps as-is, and these apps will be made available to users on the Mac through the Mac App Store. For more information, see [`Running your iOS apps in macOS`](https://developer.apple.com/documentation/Apple-Silicon/running-your-ios-apps-in-macos), and watch [`iPad and iPhone apps on Macs with Apple silicon`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2020/10114).

macOS Big Sur 11.0.1 enables you to test your iPad and iPhone apps through Xcode. Below are notes pertaining to running these apps on macOS Big Sur 11.0.1. For additional macOS 11 changes, see [`macOS Big Sur 11.0.1 Release Notes`](macos-big-sur-11_0_1-release-notes.md).

##### General

###### Known Issues

- iOS apps which don’t support iPad multitasking might display certain content in an incorrect orientation. (64660250)
- `WebGL` content in [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) might experience reduced performance. (70587571)
- Apps that specify `LSMinimumSystemVersion` in their `Info.plist` will be held to that value when running on macOS. Use the `MinimumOSVersion` `Info.plist` key. (56477669)
- When [`NSAttributedString`](https://developer.apple.com/documentation/Foundation/NSAttributedString) loads HTML, the runloop might not run. (56722469)
- Don’t assume the user’s home directory is in `/private`. (59908476)
- Methods that aren’t declared but are present on iOS such as [`allHeaderFields`](https://developer.apple.com/documentation/Foundation/HTTPURLResponse/allHeaderFields) or [`statusCode`](https://developer.apple.com/documentation/Foundation/HTTPURLResponse/statusCode) aren’t present on macOS. Instead, use the declared methods on [`HTTPURLResponse`](https://developer.apple.com/documentation/Foundation/HTTPURLResponse). (61076809)
- iOS applications on macOS use slide-over and split-screen capabilities to resize windows. Your windows might be created in a state that doesn’t match the UIScreen, as though the application was launched in a split or slide-over. (61219476)
- Device validation by checking for paths such as `/usr/libexec/sftp-server` or `/usr/sbin/sshd` isn’t supported. (62360582)
- App content might be visible during a resize. Don’t rely on your content being blurred like it is when resizing a split on iPad. (63582198)
- Don’t assume via runtime checks like [`NSClassFromString(_:)`](https://developer.apple.com/documentation/Foundation/NSClassFromString(_:)) that [`NSViewController`](https://developer.apple.com/documentation/AppKit/NSViewController) won’t be present. (63995458)
- [`CATransaction`](https://developer.apple.com/documentation/QuartzCore/CATransaction) commits might be delayed until an appropriate time. Don’t make assumptions about the timing of commits and instead use appropriate transaction or animation completion handlers to order your work. (64013629)
- Don’t assume that `/var/mobile exists`. (64650450)
- Ensure apps using [`WKWebView`](https://developer.apple.com/documentation/WebKit/WKWebView) and [`UIWebView`](https://developer.apple.com/documentation/UIKit/UIWebView) correctly handle JavaScript mouse or pointer events. This can be alternatively tested by using a mouse or trackpad with iPad. (64668138)
- Ensure you’ve registered your Mac with Apple silicon’s hardware identifier (available in the System Information app Hardware > Provisioning UDID field) in your account on [`https://developer.apple.com/account`](https://developer.apple.comhttps://developer.apple.com/account). Find the archive in the Organizer window, click on Distribute App, select either “Ad Hoc” or “Development,” choose your distribution options, select “Automatically manage signing,” and proceed through the remainder of the distribution assistant to create an IPA. Once you’ve created the IPA, you can transfer it to your Mac with Apple silicon, and double-click it to install. During the app’s first launch, macOS prompts you to open the Security & Privacy preferences pane to enable the app. To see the launch button in the preferences pane, make sure your Mac is configured to only allow apps from the App Store and identified developers. (68513041, 68528315)

## See Also

- [macOS Big Sur 11.5 Release Notes](macos-big-sur-11_5-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.4 Release Notes](macos-big-sur-11_4-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.3 Release Notes](macos-big-sur-11_3-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.2 Release Notes](macos-big-sur-11_2-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.1 Release Notes](macos-big-sur-11_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.0.1 Release Notes](macos-big-sur-11_0_1-release-notes.md)
  Update your apps to use new features, and test your apps against API changes.
- [macOS Big Sur 11.0.1 Universal Apps Release Notes](macos-big-sur-11_0_1-universal-apps-release-notes.md)
  Update your apps to support Macs with Apple silicon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/macos-release-notes/macos-big-sur-11_0_1-ios-ipados-apps-on-mac-release-notes)*