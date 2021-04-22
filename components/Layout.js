import Head from 'next/head'
import styles from '../styles/Layout.module.css'

const Layout = ({ title, description, children, keywords }) => {
  return (
    <div>
      <Head>
        <title>{title}</title>
        <meta name='keywords' content={keywords} />
        <meta name='description' content={description} />
      </Head>
      <div className={styles.container}>{children}</div>
    </div>
  )
}

Layout.defaultProps = {
  title: 'Dj events around the space',
  keywords: 'Music, Party, Events',
  description: 'get all events here',
}

export default Layout
