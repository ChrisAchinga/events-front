import Head from 'next/head'
import {useRouter} from 'next/router'
import Header from './Header'
import Footer from './Footer'
import styles from '@/styles/Layout.module.css'

import Showcase from '@/components/Showcase'

const Layout = ({ title, description, children, keywords }) => {
  const router = useRouter()
  return (
    <div>
      <Head>
        <title>{title}</title>
        <meta name='keywords' content={keywords} />
        <meta name='description' content={description} />
      </Head>
      <Header />
      {/* show showcase component only on home page */}
      {router.pathname === '/' && <Showcase />}
      <div className={styles.container}>{children}</div>
      <Footer />
    </div>
  )
}

Layout.defaultProps = {
  title: 'Dj events around the space',
  keywords: 'Music, Party, Events',
  description: 'get all events here',
}

export default Layout
