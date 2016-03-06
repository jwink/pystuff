
import re

x="$10000"

z=re.match('^(\$|)([1-9]\d{0,2}(\,\d{3})*|([1-9]\d*))(\.\d{2})?$',x)

y=re.match('^(\$|)[1-9]\d{0,2}', x)

print y.group(0)

startWord = "The"
endWord = "jumped"

x="The cat jumped over the moon"

x = x.replace(" ","")

z=re.search('(?<=' + startWord +').+(?=' + endWord + ')', x)

print z.group(0)


def getMiddlePart(startWord, endWord, searchString):
  return re.search('(?<=' + startWord +').+(?=' + endWord + ')', searchString).group(0)

def getEndPart(startWord, searchString):
  return re.search('(?<=' + startWord +').+', searchString).group(0)

def getStartPart(endWord, searchString):
  return re.search('.+(?=' + endWord + ')', searchString).group(0)


searchString = 'Thecatjumpedoverthemoon'

print getMiddlePart("The", "the", searchString)


new_string = 'loan amount: $ 120, 243, 456 .00 24 is this abc 450.689 def 42.98'

def onlyNumParts(searchString):
  num_parts = re.findall('[$\d,.\s]', searchString)
  print num_parts
  return "".join(num_parts)


new_re = re.findall('[$\d,.]', new_string)

print "".join(new_re)

print re.findall('(?<=' + startWord +').+(?=' + endWord + ')', searchString)


one_num = getMiddlePart("loa", "th", new_string)
one_num = getMiddlePart("ab", "de", new_string)
one_num = getEndPart("de", new_string)
one_num = getStartPart("abc", new_string)

print one_num
print onlyNumParts(one_num)


# findall could work.  makes the searching simpler.  need to clean afterwards

