# Security Guidelines

## Environment Variables

**CRITICAL:** Never commit sensitive information to the repository!

### Required Environment Variables

The following environment variables must be set in Heroku Config Vars (or your `.env` file for local development):

```bash
# Django Settings
SECRET_KEY=your-secret-key-here-use-strong-random-string
DEBUG=False  # MUST be False in production!

# Database
DATABASE_URL=postgresql://username:password@host:port/database

# Cloudinary (for media storage)
CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name

# CSRF Protection
CSRF_TRUSTED_ORIGINS=https://your-domain.herokuapp.com
```

### Setting Environment Variables on Heroku

```bash
heroku config:set SECRET_KEY="your-secret-key"
heroku config:set DEBUG=False
heroku config:set DATABASE_URL="your-database-url"
heroku config:set CLOUDINARY_URL="your-cloudinary-url"
heroku config:set CSRF_TRUSTED_ORIGINS="https://your-domain.herokuapp.com"
```

## Security Features Enabled

### Production Security (when DEBUG=False):
- ✅ HTTPS/SSL redirect enforced
- ✅ Secure cookies (SESSION_COOKIE_SECURE, CSRF_COOKIE_SECURE)
- ✅ XSS filter enabled
- ✅ Content type nosniff
- ✅ X-Frame-Options set to DENY
- ✅ HSTS (HTTP Strict Transport Security) enabled for 1 year
- ✅ HSTS preload and subdomains included

### Django Security Features:
- ✅ CSRF protection enabled
- ✅ Password validation
- ✅ SQL injection protection (ORM)
- ✅ Clickjacking protection
- ✅ Cross-site scripting (XSS) protection

## Files That Should NEVER Be Committed

The `.gitignore` file prevents these from being committed:

- `.env` - Contains all sensitive environment variables
- `db.sqlite3` - Local database file
- `*.pyc` - Python bytecode
- `__pycache__/` - Python cache
- `/media` - User-uploaded files
- `/staticfiles` - Collected static files
- `*.pem`, `*.key`, `*.cert` - SSL certificates and keys
- `secrets.json`, `credentials.json` - Credential files

## Checking for Sensitive Data

Before committing, always check:

```bash
# Check what files will be committed
git status

# Check the diff for sensitive data
git diff

# Never commit these patterns:
# - SECRET_KEY = 'actual-secret-key'
# - password = 'actual-password'
# - API keys or tokens
# - Database URLs with credentials
```

## Local Development

Create a `.env` file in the project root (it's in `.gitignore`):

```bash
# .env (local development only - NEVER COMMIT THIS FILE!)
SECRET_KEY=django-insecure-local-dev-key-change-this
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
CLOUDINARY_URL=cloudinary://your-local-cloudinary-url
```

## Reporting Security Issues

If you discover a security vulnerability, please email the maintainer directly. Do not create a public GitHub issue.

## Security Checklist

Before deploying to production:

- [ ] DEBUG is set to False in Heroku Config Vars
- [ ] SECRET_KEY is strong and unique (not the default)
- [ ] All sensitive data is in environment variables
- [ ] `.gitignore` is properly configured
- [ ] No `.env` files are committed
- [ ] HTTPS is enforced (SSL certificate active on Heroku)
- [ ] CSRF_TRUSTED_ORIGINS includes your domain
- [ ] Database credentials are secure
- [ ] Admin panel uses strong password
- [ ] All dependencies are up to date

## Regular Security Maintenance

- Update dependencies regularly: `pip list --outdated`
- Monitor Django security releases
- Review access logs periodically
- Rotate SECRET_KEY if compromised
- Review and update permissions

