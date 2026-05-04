<?php
/**
 * USAM Nîmes Gard — Functions
 *
 * Point d'entrée du thème : enqueue assets, supports, custom post types, helpers.
 */

defined( 'ABSPATH' ) || exit;

define( 'USAM_THEME_VERSION', '0.1.0' );
define( 'USAM_THEME_DIR', get_template_directory() );
define( 'USAM_THEME_URI', get_template_directory_uri() );

require_once USAM_THEME_DIR . '/inc/setup.php';
require_once USAM_THEME_DIR . '/inc/assets.php';
require_once USAM_THEME_DIR . '/inc/menus.php';
require_once USAM_THEME_DIR . '/inc/cpt-joueur.php';
require_once USAM_THEME_DIR . '/inc/cpt-match.php';
require_once USAM_THEME_DIR . '/inc/cpt-partenaire.php';
require_once USAM_THEME_DIR . '/inc/helpers.php';
