#! /bin/sh

cat << EOF | sed -e "s/FACEBOOK_ID/${FACEBOOK_ID}/; s/FACEBOOK_SECRET/${FACEBOOK_SECRET}/; " >> app/web/fixtures/oauth_fixtures.yaml
- fields:
    client_id: 'FACEBOOK_ID'
    key: ''
    name: Facebook
    provider: facebook
    secret: FACEBOOK_SECRET
    sites: [1, 2]
  model: socialaccount.socialapp
  pk: 1
EOF
