# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

1. **Do Not** open a public issue
2. Email your findings to adnan.rp359@gmail.com
3. Include detailed steps to reproduce the vulnerability
4. Allow some time for the issue to be addressed before public disclosure

## Security Considerations

### Password Generation

This application uses Python's `random` module which relies on the operating system's source of randomness. While this is suitable for most purposes, here are some security considerations:

1. For cryptographic applications, modify the code to use the `secrets` module:
```python
import secrets

def generate_password(length, chars):
    return ''.join(secrets.choice(chars) for _ in range(length))
```

2. The application never stores or transmits passwords
3. Passwords are only held in memory temporarily
4. The clipboard is not automatically cleared (users should be aware of this)

### Best Practices

1. Always use generated passwords only once
2. Use different passwords for different accounts
3. Consider using a password manager
4. Regular security updates are recommended
5. Be cautious when copying passwords to clipboard

## Dependencies

We regularly update dependencies to patch security vulnerabilities. To check for known vulnerabilities in dependencies:

```bash
pip install safety
safety check
```