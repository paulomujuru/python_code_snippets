
def html_tag(tag):

    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag, msg))

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test Paragraph!')



backgroud color{

    gainsboro
}


 .tile.mt-2
    .tile.is-vertical.is-12
      .tile.px-2.py-2
        VoiceStatus(:agents="voiceStatus")