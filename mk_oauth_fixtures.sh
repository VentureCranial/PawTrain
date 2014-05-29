#! /bin/sh

# Create the fixtures for oauth based on the environment settings
# so that they don't go into code.
#

cat << EOF | sed -e "s/FACEBOOK_ID/${FACEBOOK_ID}/;
    s/FACEBOOK_SECRET/${FACEBOOK_SECRET}/;
    s/LINKEDIN_ID/${LINKEDIN_ID}/;
    s/LINKEDIN_SECRET/${LINKEDIN_SECRET}/;
    s/TWITTER_ID/${TWITTER_ID}/;
    s/TWITTER_SECRET/${TWITTER_SECRET}/;
    " > app/web/fixtures/oauth_fixtures.yaml
- fields:
    client_id: 'FACEBOOK_ID'
    key: ''
    name: Facebook
    provider: facebook
    secret: FACEBOOK_SECRET
    sites: [1, 2]
  model: socialaccount.socialapp
  pk: 1
- fields:
    client_id: LINKEDIN_ID
    key: ''
    name: Linked In
    provider: linkedin_oauth2
    secret: LINKEDIN_SECRET
    sites: [2, 1]
  model: socialaccount.socialapp
  pk: 2
- fields:
    client_id: TWITTER_ID
    key: ''
    name: Twitter
    provider: twitter
    secret: TWITTER_SECRET
    sites: [2, 1]
  model: socialaccount.socialapp
  pk: 3
EOF
