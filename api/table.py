from models import Relation, Uname

print "Relations:"
for r in Relation.objects.all():
    print r

print "------------------------"
print "Users:"

for u in Uname.objects.all():
    print u
