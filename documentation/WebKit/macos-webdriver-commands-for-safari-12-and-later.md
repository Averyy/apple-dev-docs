# macOS WebDriver Commands for Safari 12 and later

**Framework**: WebKit  
**Role**: Article

Test your web content using the WebDriver commands supported by Safari 12 and later.

## Overview

This table lists the method and the URI template (the *endpoint*) that executes each command. The [macOS WebDriver Commands for Safari 11.1 and earlier](./macos-webdriver-commands-for-safari-11-1-and-earlier.md) support the Selenium JSON Wire Protocol. The [macOS WebDriver Commands for Safari 12 and later](./macos-webdriver-commands-for-safari-12-and-later.md) support the the [W3C WebDriver protocol](https://www.w3.org/TR/webdriver/#list-of-endpoints).

All URI templates listed here are supported by the `safaridriver` tool included with Safari 12 and later. For more information on the tool, see [About WebDriver for Safari](./about-webdriver-for-safari.md).

| Method | URI template | Supported | Safari Technology Preview release, Safari version |
| --- | --- | --- | --- |
| POST | [/session](https://www.w3.org/TR/webdriver/#dfn-creating-a-new-session) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| DELETE | [/session/{session id}](https://www.w3.org/TR/webdriver/#dfn-delete-session) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/status](https://www.w3.org/TR/webdriver/#dfn-status) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/timeouts](https://www.w3.org/TR/webdriver/#dfn-get-timeouts) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/timeouts](https://www.w3.org/TR/webdriver/#dfn-timeouts) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/url](https://www.w3.org/TR/webdriver/#dfn-navigate-to) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/url](https://www.w3.org/TR/webdriver/#dfn-get-current-url) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/back](https://www.w3.org/TR/webdriver/#dfn-back) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/forward](https://www.w3.org/TR/webdriver/#dfn-forward) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/refresh](https://www.w3.org/TR/webdriver/#dfn-refresh) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/title](https://www.w3.org/TR/webdriver/#dfn-get-title) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/window](https://www.w3.org/TR/webdriver/#dfn-get-window-handle) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| DELETE | [/session/{session id}/window](https://www.w3.org/TR/webdriver/#dfn-close-window) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/window](https://www.w3.org/TR/webdriver/#dfn-switch-to-window) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/window/handles](https://www.w3.org/TR/webdriver/#dfn-get-window-handles) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/frame](https://www.w3.org/TR/webdriver/#dfn-switch-to-frame) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/frame/parent](https://www.w3.org/TR/webdriver/#dfn-switch-to-parent-frame) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/window/rect](https://www.w3.org/TR/webdriver/#dfn-get-window-rect) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/window/rect](https://www.w3.org/TR/webdriver/#dfn-set-window-rect) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/window/maximize](https://www.w3.org/TR/webdriver/#dfn-maximize-window) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/window/maximize](https://www.w3.org/TR/webdriver/#dfn-minimize-window) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/window/fullscreen](https://www.w3.org/TR/webdriver/#dfn-fullscreen-window) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/element/active](https://www.w3.org/TR/webdriver/#dfn-get-active-element) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/element](https://www.w3.org/TR/webdriver/#dfn-find-element) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/elements](https://www.w3.org/TR/webdriver/#dfn-find-elements) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/element/{element id}/element](https://www.w3.org/TR/webdriver/#dfn-find-element-from-element) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/element/{element id}/elements](https://www.w3.org/TR/webdriver/#dfn-find-elements-from-element) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/element/{element id}/selected](https://www.w3.org/TR/webdriver/#dfn-is-element-selected) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/element/{element id}/attribute/{name}](https://www.w3.org/TR/webdriver/#dfn-get-element-attribute) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/element/{element id}/property/{name}](https://www.w3.org/TR/webdriver/#dfn-get-element-property) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/element/{element id}/css/{property name}](https://www.w3.org/TR/webdriver/#dfn-get-element-css-value) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/element/{element id}/text](https://www.w3.org/TR/webdriver/#dfn-get-element-text) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/element/{element id}/name](https://www.w3.org/TR/webdriver/#dfn-get-element-tag-name) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/element/{element id}/rect](https://www.w3.org/TR/webdriver/#dfn-get-element-rect) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/{element id}/enabled](https://www.w3.org/TR/webdriver/#dfn-is-element-enabled) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/element/{element id}/click](https://www.w3.org/TR/webdriver/#dfn-element-click) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/element/{element id}/clear](https://www.w3.org/TR/webdriver/#dfn-element-clear) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/element/{element id}/value](https://www.w3.org/TR/webdriver/#dfn-element-send-keys) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/source](https://www.w3.org/TR/webdriver/#dfn-get-page-source) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/execute/sync](https://www.w3.org/TR/webdriver/#dfn-execute-script) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/execute/async](https://www.w3.org/TR/webdriver/#dfn-execute-async-script) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/cookie](https://www.w3.org/TR/webdriver/#dfn-get-all-cookies) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/cookie/{name}](https://www.w3.org/TR/webdriver/#dfn-get-named-cookie) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/cookie](https://www.w3.org/TR/webdriver/#dfn-adding-a-cookie) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| DELETE | [/session/{session id}/cookie/{name}](https://www.w3.org/TR/webdriver/#dfn-delete-cookie) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| DELETE | [/session/{session id}/cookie](https://www.w3.org/TR/webdriver/#dfn-delete-all-cookies) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/actions](https://www.w3.org/TR/webdriver/#dfn-perform-actions) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| DELETE | [/session/{session id}/actions](https://www.w3.org/TR/webdriver/#dfn-release-actions) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/alert/dismiss](https://www.w3.org/TR/webdriver/#dfn-dismiss-alert) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/alert/accept](https://www.w3.org/TR/webdriver/#dfn-accept-alert) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/alert/text](https://www.w3.org/TR/webdriver/#dfn-get-alert-text) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| POST | [/session/{session id}/alert/text](https://www.w3.org/TR/webdriver/#dfn-send-alert-text) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/screenshot](https://www.w3.org/TR/webdriver/#dfn-take-screenshot) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |
| GET | [/session/{session id}/element/{element id}/screenshot](https://www.w3.org/TR/webdriver/#dfn-take-element-screenshot) | ✓ | [60](https://developer.apple.com/safari/technology-preview/release-notes/#r60), [12](https://developer.apple.com/safari/whats-new/) |

## See Also

### WebDriver
- [macOS WebDriver Commands for Safari 11.1 and earlier](./macos-webdriver-commands-for-safari-11-1-and-earlier.md)
  Test your web content using the WebDriver commands supported by Safari 11.1 and earlier.
- [About WebDriver for Safari](./about-webdriver-for-safari.md)
  Enhance testing of your web content using Safari’s enhancements to WebDriver.
- [Testing with WebDriver in Safari](./testing-with-webdriver-in-safari.md)
  Enable WebDriver and run a test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/webkit/macos-webdriver-commands-for-safari-12-and-later)*