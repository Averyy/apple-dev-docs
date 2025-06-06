# Defining a custom URL scheme for your app

**Framework**: Xcode

Use specially formatted URLs to link to content within your app.

#### Overview

Custom URL schemes provide a way to reference resources inside your app. Users tapping a custom URL in an email, for example, launch your app in a specified context. Other apps can also trigger your app to launch with specific context data; for example, a photo library app might display a specified image.

While custom URL schemes are an acceptable form of deep linking, universal links are strongly recommended. For more information on universal links, see [`Allowing apps and websites to link to your content`](allowing-apps-and-websites-to-link-to-your-content.md).

Apple supports common schemes associated with system apps, such as `mailto`, `tel`, `sms`, and `facetime`. You can define your own custom scheme and register your app to support it.

> ⚠️ **Warning**: URL schemes offer a potential attack vector into your app, so make sure to validate all URL parameters and discard any malformed URLs. In addition, limit the available actions to those that don’t risk the user’s data. For example, don’t allow other apps to directly delete content or access sensitive information about the user. When testing your URL-handling code, make sure your test cases include improperly formatted URLs.

URL schemes offer a potential attack vector into your app, so make sure to validate all URL parameters and discard any malformed URLs. In addition, limit the available actions to those that don’t risk the user’s data. For example, don’t allow other apps to directly delete content or access sensitive information about the user. When testing your URL-handling code, make sure your test cases include improperly formatted URLs.

To support a custom URL scheme:

1. Define the format for your app’s URLs.
2. Register your scheme so that the system directs appropriate URLs to your app.
3. Handle the URLs that your app receives.

URLs must start with your custom scheme name. Add parameters for any options your app supports. For example, a photo library app might define a URL format that includes the name or index of a photo album to display. Examples of URLs for such a scheme could include the following:

```other
myphotoapp:albumname?name="albumname"
myphotoapp:albumname?index=1
```

Clients craft URLs based on your scheme and ask your app to open them by calling the [`open(_:options:completionHandler:)`](https://developer.apple.com/documentation/UIKit/UIApplication/open(_:options:completionHandler:)) method of [`UIApplication`](https://developer.apple.com/documentation/UIKit/UIApplication). Clients can ask the system to inform them when your app opens the URL.

```swift
let url = URL(string: "myphotoapp:Vacation?index=1")

UIApplication.shared.open(url!) { (result) in
    if result {
       // The URL was delivered successfully!
    }
}
```

##### Register Your Url Scheme

URL scheme registration specifies which URLs to redirect to your app. Register your scheme in Xcode from the Info tab of your project settings. Update the URL Types section to declare all of the URL schemes your app supports, as shown in the following illustration.

- In the URL Schemes box, specify the prefix you use for your URLs.
- Choose a role for your app: either an editor role for URL schemes you define, or a viewer role for schemes your app adopts but doesn’t define.
- Specify an identifier for your app.

![Screenshot of Xcode showing the URL Types section with a URL that reads “com.example.myphotoapp.”](https://docs-assets.developer.apple.com/published/33d1c93a0355274a4c27075ab11717f7/defining-a-custom-url-scheme-for-your-app-1%402x.png)

The identifier you supply with your scheme distinguishes your app from others that declare support for the same scheme. To ensure uniqueness, specify a reverse DNS string that incorporates your company’s domain and app name. Although using a reverse DNS string is a best practice, it doesn’t prevent other apps from registering the same scheme and handling the associated links. Use universal links instead of custom URL schemes to define links that are uniquely associated with your website.

> **Note**: If multiple apps register the same scheme, the app the system targets is undefined. There’s no mechanism to change the app or to change the order apps appear in a Share sheet.

If multiple apps register the same scheme, the app the system targets is undefined. There’s no mechanism to change the app or to change the order apps appear in a Share sheet.

Some URL schemes are reserved for system use. The system directs well-known types of URLs to the corresponding system apps, and well-known `http–`based URLs to specific apps such as Maps, YouTube, and Music. For information about the schemes supported by Apple, see [`Apple URL Scheme Reference`](https://developer.apple.comhttps://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007899).

##### Handle Incoming Urls

When another app opens a URL containing your custom scheme, the system launches your app, if necessary, and brings it to the foreground. The system delivers the URL to your app by calling your app delegate’s [`application(_:open:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:open:options:)) method. Add code to the method to parse the contents of the URL and take appropriate actions. To ensure the URL is parsed correctly, use [`NSURLComponents`](https://developer.apple.com/documentation/Foundation/NSURLComponents) APIs to extract the components. Obtain additional information about the URL, such as which app opened it, from the system-provided options dictionary.

```swift
func application(_ application: UIApplication,
                 open url: URL,
                 options: [UIApplicationOpenURLOptionsKey : Any] = [:] ) -> Bool {

    // Determine who sent the URL.
    let sendingAppID = options[.sourceApplication]
    print("source application = \(sendingAppID ?? "Unknown")")

    // Process the URL.
    guard let components = NSURLComponents(url: url, resolvingAgainstBaseURL: true),
        let albumPath = components.path,
        let params = components.queryItems else {
            print("Invalid URL or album path missing")
            return false
    }

    if let photoIndex = params.first(where: { $0.name == "index" })?.value {
        print("albumPath = \(albumPath)")
        print("photoIndex = \(photoIndex)")
        return true
    } else {
        print("Photo index missing")
        return false
    }
}
```

The system also uses your app delegate’s [`application(_:open:options:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:open:options:)) method to open custom file types that your app supports.

If your app has opted into [`Scenes`](https://developer.apple.com/documentation/UIKit/scenes), and your app isn’t running, the system delivers the URL to the [`scene(_:willConnectTo:options:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:willConnectTo:options:)) delegate method after launch, and to [`scene(_:openURLContexts:)`](https://developer.apple.com/documentation/UIKit/UISceneDelegate/scene(_:openURLContexts:)) when your app opens a URL while running or suspended in memory.

```swift
func scene(_ scene: UIScene, 
           willConnectTo session: UISceneSession, 
           options connectionOptions: UIScene.ConnectionOptions) {

    // Determine who sent the URL.
    if let urlContext = connectionOptions.urlContexts.first {

        let sendingAppID = urlContext.options.sourceApplication
        let url = urlContext.url
        print("source application = \(sendingAppID ?? "Unknown")")
        print("url = \(url)")

        // Process the URL similarly to the UIApplicationDelegate example.
    }

    /*
     *
     */
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/xcode/defining-a-custom-url-scheme-for-your-app)*