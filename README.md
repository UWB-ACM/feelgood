# feelgood

An example project for UWB Hacks the Cloud, ACM's on-campus hackathon.

## S3, CloudFront, and Route53 Configuration for Static Website

We used to the following resources as a guide for configuring S3 buckets to host the subscription website:

[Setting Up a Static Website Using a Custom Domain Name Registered with Route 53](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html)<br>
This guide will walk you through how to register a custom domain using Route 53 and create/configure two S3 buckets to serve as containers for the contents of your website.

[Setting up a Static Website](https://docs.aws.amazon.com/AmazonS3/latest/dev/HostingWebsiteOnS3Setup.html)<br>
If you don't wish to buy a custom domain, use this guide instead. Your website will still be publicly accessible with a link that resembles the following: `http://your-bucket-name.s3-website-your-aws-region.amazonaws.com`

[Obtaining an SSL Certificate for a Custom Domain](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-serve-static-website/)<br>
This guide explains how to use CloudFront to request an SSL certificate for your custom domain in order to serve content over an HTTPS protocol. Make sure to scroll down to the section titled `Using a website endpoint as the origin with anonymous (public) access allowed`, which aligns with the configuration outlined in the two previous S3 setup guides.

[Updating Existing Content with a CloudFront Distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/UpdatingExistingObjects.html)<br>
If using CloudFront to serve your site over HTTPS, you will find updating the content of the site is not as simple as changing out the files in the S3 bucket due to CloudFront's caching properties. This guide outlines two workarounds: using versioned file names, and [invalidating the object](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Invalidation.html) within CloudFront which prompts it to reload objects the source.

[Collecting and Submitting Form Data to Other AWS Services using HTML and jQuery AJAX requsts](https://aws.amazon.com/blogs/architecture/create-dynamic-contact-forms-for-s3-static-websites-using-aws-lambda-amazon-api-gateway-and-amazon-ses/)<br>
The `Your “Contact Us” Form` section of this guide covers how to create a simple web form using HTML, and `Connecting it all Together` covers how to use [jQuery AJAX calls](https://api.jquery.com/jquery.ajax/) to send the data collected in the form to other AWS services to complete the subscription process.
