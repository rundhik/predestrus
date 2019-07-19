from estrus import apl, db, User, Wilayah, Anggota, Sapi, migrate

@apl.shell_context_processor
def make_shell_context():
    return dict(app=apl, db=db, User=User, migrate=migrate)