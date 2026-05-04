<?php
/**
 * Configuration du thème : supports, image sizes, i18n.
 */

defined( 'ABSPATH' ) || exit;

add_action( 'after_setup_theme', function () {
	load_theme_textdomain( 'usam', USAM_THEME_DIR . '/languages' );

	add_theme_support( 'title-tag' );
	add_theme_support( 'post-thumbnails' );
	add_theme_support( 'html5', [ 'search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script' ] );
	add_theme_support( 'custom-logo', [
		'height'      => 200,
		'width'       => 200,
		'flex-height' => true,
		'flex-width'  => true,
	] );
	add_theme_support( 'responsive-embeds' );
	add_theme_support( 'editor-styles' );

	add_image_size( 'usam-hero', 1920, 1080, true );
	add_image_size( 'usam-card', 800, 600, true );
	add_image_size( 'usam-portrait', 600, 800, true );
	add_image_size( 'usam-thumb-square', 400, 400, true );
} );

// Optimisations propreté front
add_action( 'init', function () {
	remove_action( 'wp_head', 'wp_generator' );
	remove_action( 'wp_head', 'wlwmanifest_link' );
	remove_action( 'wp_head', 'rsd_link' );
	remove_action( 'wp_head', 'wp_shortlink_wp_head' );
} );

// Désactiver les emojis WordPress (perf + cohérence design)
add_action( 'init', function () {
	remove_action( 'wp_head', 'print_emoji_detection_script', 7 );
	remove_action( 'wp_print_styles', 'print_emoji_styles' );
} );
