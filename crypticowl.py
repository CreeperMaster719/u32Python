def close_far(a, b, c):
  if(abs(abs(a)-abs(b)) == 1 or abs(abs(b)-abs(c)) == 1 or abs(abs(a)-abs(c)) == 1):
    if(abs(abs(a)-abs(b)) >= 2 or abs(abs(b)-abs(c)) >= 2 or abs(abs(a)-abs(c)) >= 2):
      return True
    else:
      return False
  else:
    return False

if(close_far(1,2,3)):
    print "Success!"