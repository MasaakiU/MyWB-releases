# MyWB Privacy Policy

Effective date: August 11, 2026

MyWB is a local desktop application for research use. It is designed to run
on your computer and process files that you choose to open, create, or save.

## Data Collection

MyWB does not require a user account in its account-free releases and does not
ask for your name, email address, postal address, or payment information.

MyWB does not transmit your research data, file contents, images, settings,
labels, or measurements to the developer or an online service.

MyWB does not include individual behavioral analytics, advertising identifiers,
persistent remote tracking, or automatic crash reporting.

Limited technical request data and de-identified aggregate service totals may
be processed when MyWB performs the online checks described below. This data
is not used for advertising or behavioral profiling.

## Local Files and Research Data

Images, MyWB files, SVG exports, settings, labels, measurements, and other
user-created data remain on your computer unless you choose to share them.

MyWB may read files that you open and may write files that you save or export.
When you use PowerPoint-to-MyWB import, SVG data is read either from the local
clipboard by `Paste MyWB from PowerPoint` or from the `.pptx` file you select
by `Import MyWB from PowerPoint File`. The selected PowerPoint file, its file
name and path, and the imported SVG data are processed locally and are not
transmitted as part of license verification.

Some MyWB SVG files may contain embedded image data and MyWB session metadata.
This allows a session to be reopened later.

## Local Settings

MyWB may store application settings locally on your computer, such as user
preferences and recently used file or folder locations. These settings are
stored using the operating system's standard application settings storage and
are not transmitted to the developer.

## Network Access

MyWB does not require a continuous internet connection for local file
processing. Update checks and license or service status checks require an
occasional internet connection.

### Update Checks

When MyWB starts, or when you select Check for Updates, it may make an HTTPS
GET request to a MyBioApps-operated update service delivered through
Cloudflare. This request retrieves the version number of the latest stable
MyWB release. MyWB identifies its application name and version in the
User-Agent header.

The update-check request has no request body and does not include:

- a Cookie or Authorization header;
- an account, device, or installation identifier;
- a hardware fingerprint; or
- your files, file contents, file names, file paths, images, research data,
  settings, labels, annotations, or measurements.

Cloudflare processes the standard technical request information described
below when delivering the update service. The update service reads release
information bundled into its deployed configuration. It does not contact
GitHub while answering an update-check request and does not forward the
application's incoming User-Agent, Cookie, Authorization header, or other
application-supplied request headers to another service.

If MyWB reports that an update is available, choosing its release-page action
opens a fixed public GitHub repository address in your default browser. When
you visit that repository, GitHub receives the standard technical information
associated with your browser's direct connection. A latest-download link may
first contact the MyBioApps update service and then temporarily redirect your
browser to the versioned DMG asset hosted by GitHub. GitHub receives a direct
request from your browser when that redirect is followed.

MyWB does not automatically download or install updates unless this
functionality is explicitly added in a future release.

### License and Service Status Checks

MyWB may contact a MyWB-operated licensing service on first activation and
periodically afterward, including when a locally cached authorization is due
for renewal, near expiry, or expired. The check may also retrieve service
notices, including advance notice of licensing changes.

Quantification and PowerPoint-to-MyWB import (`Paste MyWB from PowerPoint` and
`Import MyWB from PowerPoint File`) require a successful online verification
before first use of a Premium Feature and at least once every 30 days afterward
to remain continuously available. A successful check permits offline use of
both Premium Features for up to 30 days. That period may be shorter if a
previously announced change to access takes effect sooner. If the cached
authorization expires before verification succeeds, the Premium Features
remain unavailable until a new authorization is obtained.

The licensing design uses locally cached authorization. It is not intended to
contact the service on every application launch.

The current account-free check is an HTTPS GET request with no request body.
MyWB identifies its application name and version in the User-Agent header.

Each request includes a temporary nonce generated from 32 random bytes. The
nonce is used only to bind the signed response to that request and verify the
service time.

MyWB retains the request nonce only while checking that response. Its signed
copy may remain inside the cached authorization. It is not reused as, or
converted into, a persistent identifier.

The account-free request does not include:

- a Cookie or Authorization header;
- the cached entitlement;
- an account, device, or installation identifier;
- an operating-system value; or
- a hardware fingerprint.

The account-free licensing design does not send your name, email address,
research data, file names, file paths, or a persistent hardware fingerprint.

The signed authorization returned by the service is stored locally and is not
sent back during later account-free checks.

If a future release introduces user registration, payment processing, an
account token, or a persistent installation identifier, this policy will be
updated before that information is collected.

### Technical Request Data and Request Counts

When MyWB connects to an online service, the service provider necessarily
processes standard technical information associated with the connection. This
may include:

- the IP address;
- the request date and time;
- the requested endpoint;
- HTTP headers such as the User-Agent;
- the response status; and
- network or approximate location information inferred by the provider.

The developer may be able to see aggregate request counts and short-lived
operational logs.

The developer may use de-identified aggregate update- and license-service
request totals to understand overall service activity and app-version
adoption. These totals are not used to identify or link users, devices,
installations, or activity across different days.

If an update or license check is made near application startup, those counts
may provide an approximate indication of check frequency. They are not an
exact count of application launches or days of use because checks may be
cached or skipped, requests may be retried, and some use may occur offline.

MyWB does not send a separate per-launch or daily-activity analytics event.

The update and licensing services may use Cloudflare for hosting, security,
and delivery.

Developer-accessible Cloudflare Workers logs, when enabled for security,
reliability, troubleshooting, or creation of the de-identified aggregate totals
described above, will be retained for no longer than 7 days. If temporarily
exported for these purposes, any developer-held raw copy will be deleted within
the same period.

Raw logs will not be exported to advertising or behavioral analytics services.

Aggregated operational totals that no longer relate to an IP address, request
nonce, authorization token, or individual request may be retained longer for
capacity planning, abuse prevention, and understanding overall service activity
and app-version adoption.

Cloudflare's own processing is governed by its privacy policy.

## User-Initiated Communication

If you contact the developer for support, you may choose to send screenshots,
files, crash details, or other information. Any such information is provided
by you voluntarily and is used only to respond to your request.

## Third-Party Components

MyWB includes third-party software components. Their license terms are
described in the third-party notices and license materials included with MyWB.
Online update and licensing requests may be processed by Cloudflare. The
update service does not contact GitHub while answering an update-check request.
GitHub processes direct requests when you visit the public repository or follow
a download redirect. Those providers' handling of information is governed by
their own privacy policies.

## Changes

This privacy policy may be updated for future releases of MyWB. The version
included with your copy of MyWB applies to that distribution.
