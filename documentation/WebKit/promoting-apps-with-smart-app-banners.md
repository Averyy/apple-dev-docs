# Promoting Apps with Smart App Banners

**Framework**: WebKit

Create a banner to promote your app on the App Store from a website.

#### Overview

Smart App Banners vastly improve users’ browsing experience compared to other promotional methods. In iOS, Smart App Banners  provide a consistent look and feel that users come to recognize. They trust that tapping the banner will take them to the App Store and not a third-party advertisement. They appreciate unobtrusive banners at the top of a webpage, instead of a full screen that interrupts their experience with the web content. And with a large and prominent Close button, a banner is easy to dismiss. When the user returns to the webpage, the banner doesn’t reappear.

![Smart App Banner with a View button above a web page for an app.](https://docs-assets.developer.apple.com/published/f824d208c04f48099940de5a48ccbb6c/media-3701613%402x.png)

If the app is already installed on a user’s device, the Smart App Banner intelligently changes its action, and tapping the banner simply opens the app. If the user doesn’t have your app on their device, tapping the banner takes them to the app’s entry in the App Store. When they return to your website, a progress bar appears in the banner, indicating how much longer the download will take to complete. When the app finishes downloading, the View button changes to an Open button, and tapping the banner opens the app while preserving the user’s content from your website.

![Smart App Banner with a Open button above a web page for an app.](https://docs-assets.developer.apple.com/published/ac911ef324765f30b1c4156fa16be95e/media-3701614%402x.png)

Smart App Banners automatically determine whether the user’s device supports your app. If it doesn’t, or if your app is unavailable in the user’s location, the banner doesn’t appear.

##### Implement a Smart App Banner on Your Website

To add a Smart App Banner to your website, include the following meta tag in the `head` element of each page where you’d like the banner to appear:

```javascript
<meta name="apple-itunes-app" content="app-id=myAppStoreID, app-argument=myURL">
```

You can include two comma-separated parameters in the content attribute:

Typically, it’s beneficial to retain navigational context because:

- If the user is deep within the navigational hierarchy of your website, you can pass the document’s entire URL, and then parse it in your app to reroute the user to the correct location in your app.
- If the user performs a search on your website, you can pass the query string so the user can seamlessly continue the search in your app without having to retype their query.
- If the user is in the midst of creating content, you can pass the session ID to download the web session state to your app so the user can nondestructively resume their work.

You can generate the `app-argument` parameter for each page dynamically with a server-side script. You can format it however you like, as long as it’s a valid URL.

> **Note**:  You can’t display Smart App Banners inside a frame. Banners don’t appear in the iOS simulator.

##### Provide Navigational Context to Your App

Implement the [`application(_:open:sourceApplication:annotation:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:open:sourceApplication:annotation:)): method in your app delegate, which fires when your app is launched from a URL. Then provide logic that can interpret the URL you pass. The value you set for the `app-argument` parameter is available as the [`NSURL`](https://developer.apple.com/documentation/Foundation/NSURL) [`url`](https://developer.apple.com/documentation/Foundation/NSURLComponents/url) object.

The code sample below is for a website that passes data to a native iOS app. It first detects whether the URL contains the string `/profile`. If so, it opens the profile view controller and passes the profile ID number that’s in the query string.

```objc
- (BOOL)application:(UIApplication *)application openURL:(NSURL *)url sourceApplication:(NSString *)sourceApplication annotation:(id)annotation {

    // In this example, the URL from which the user came is http://example.com/profile/?12345.

    // Determine whether the user was viewing a profile.
    if ([[url path] isEqualToString:@"/profile"]) {

        // Switch to the profile view controller.
        [self.tabBarController setSelectedViewController:profileViewController];

        // Pull the profile ID number found in the query string.
        NSString *profileID = [url query];

        // Pass the profile ID number to the profile view controller.
        [profileViewController loadProfile:profileID];

    }
    return YES;
}
```

## See Also

- [Optimizing Your Website for Safari](optimizing-your-website-for-safari.md)
  Improve your website by optimizing it for Safari.
- [Delivering Video Content for Safari](delivering-video-content-for-safari.md)
  Improve the performance and appearance of video in your website in Safari.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/promoting-apps-with-smart-app-banners)*