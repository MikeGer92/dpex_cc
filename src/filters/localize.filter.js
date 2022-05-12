import store from '../store'
import ru from '../localize/ru.json'
import en from '../localize/en.json'

const locales = {
  'ru-RU': ru,
  'en-EN': en
}

export default function localizeFilter(key) {
  const locale = store.getters.info.locale || 'ru-RU'
  return locales[locale][key] || `[Localize error]: key ${key} not found`
}