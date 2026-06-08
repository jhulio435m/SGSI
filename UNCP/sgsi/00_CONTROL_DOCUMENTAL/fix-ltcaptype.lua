function RawBlock(el)
  if el.format == 'latex' then
    local text = el.text
    -- Replace \def\LTcaptype{none} with empty definition to fix newer longtable
    text = text:gsub('\\def\\LTcaptype{none}', '\\def\\LTcaptype{}')
    return pandoc.RawBlock('latex', text)
  end
  return nil
end
