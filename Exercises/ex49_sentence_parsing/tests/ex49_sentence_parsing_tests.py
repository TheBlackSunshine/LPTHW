from nose.tools import *
from ex49_sentence_parsing import parser
from ex49_sentence_parsing import lexicon

def test_sentence():
	s = parser.Sentence(('noun', 'princess'), ('verb', 'kills'), ('noun', 'bear'))
	assert_equals(s.subject, 'princess')
	assert_equals(s.verb, 'kills')
	assert_equals(s.object, 'bear')
	
def test_peek():
	word_list = lexicon.scan('princess')
	assert_equals(parser.peek(word_list), 'noun')
	assert_equals(parser.peek(None), None)
	
def test_match():
	word_list = lexicon.scan('go')
	assert_equals(parser.match(word_list, 'verb'), ('verb', 'go'))
	assert_equals(parser.match(word_list, 'stop'), None)
	assert_equals(parser.match(None, 'noun'), None)
	
def test_skip():
    word_list = lexicon.scan('bear eat door')
    assert_equal(word_list, [('noun', 'bear'), ('verb', 'eat'), ('noun', 'door')])
    parser.skip(word_list, 'noun')
    assert_equal(word_list, [('verb', 'eat'), ('noun', 'door')])

def test_parse_verb():
    word_list = lexicon.scan('it eat door')
    assert_equal(parser.parse_verb(word_list), ('verb', 'eat'))
    word_list = lexicon.scan('bear eat door')
    assert_raises(parser.ParserError, parser.parse_verb, word_list)

def test_parse_object():
    word_list = lexicon.scan('the door')
    assert_equal(parser.parse_object(word_list), ('noun', 'door'))
    word_list = lexicon.scan('the east')
    assert_equal(parser.parse_object(word_list), ('direction', 'east'))
    word_list = lexicon.scan('the it')
    assert_raises(parser.ParserError, parser.parse_object, word_list)

def test_parse_subject():
    word_list = lexicon.scan('eat door')
    subj = ('noun', 'bear')
    s = parser.parse_subject(word_list, subj)

def test_parse_sentence():
    word_list = lexicon.scan('the bear eat door')
    s = parser.parse_sentence(word_list)
    word_list = lexicon.scan('in eat door')
    s = parser.parse_sentence(word_list)
    word_list = lexicon.scan('north eat door')
    assert_raises(parser.ParserError, parser.parse_sentence, word_list)

def test_unknown_words():
    word_list = lexicon.scan('xxx the xxx bear xxx eat xxx door xxx')
    s = parser.parse_sentence(word_list)
    assert_equal(s, ('bear', 'eat', 1, 'door'))

def test_numbers():
    word_list = lexicon.scan('xxx the xxx bear xxx eat xxx 5 xxx door xxx')
    s = parser.parse_sentence(word_list)
    assert_equal(s, ('bear', 'eat', 5, 'door'))