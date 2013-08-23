import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
os.environ['DATABASE_URL'] = 'sqlite://'
